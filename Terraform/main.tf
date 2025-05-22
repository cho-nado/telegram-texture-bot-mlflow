resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Создание сети и подсети
resource "yandex_vpc_network" "default" {
  name = "default-network"
}

resource "yandex_vpc_subnet" "default" {
  name           = "default-subnet"
  zone           = "ru-central1-b"
  network_id     = yandex_vpc_network.default.id
  v4_cidr_blocks = ["10.0.0.0/24"]
}

# Модуль бакета
module "s3_bucket" {
  source      = "./modules/s3"
  bucket_name = coalesce(var.bucket_name, "bucket-${random_id.bucket_suffix.hex}")
  acl         = var.bucket_acl
}

# Виртуальная машина
data "yandex_compute_image" "ubuntu" {
  family = "ubuntu-2204-lts"
}

resource "yandex_compute_instance" "vm" {
  name        = "s3-client-vm"
  platform_id = "standard-v1"
  zone        = "ru-central1-b"

  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = data.yandex_compute_image.ubuntu.id
    }
  }

  network_interface {
    subnet_id = yandex_vpc_subnet.default.id
    nat       = true
  }

  metadata = {
    user-data = file("${path.module}/cloud-init.yaml")
  }
}