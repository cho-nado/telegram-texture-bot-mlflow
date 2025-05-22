# Terraform-project using Yandex Cloud

## 📦 Description of the project

This project is an example of Infrastructure as Code (IaC) using Terraform, designed to deploy resources in Yandex Cloud. The setup automatically creates:

- **S3 Bucket** — a cloud-based file storage;
- **Virtual Machine (VM)** — configured via cloud-init, with access to the S3 bucket using AWS CLI;
- **Network infrastructure** — including a VPC and subnet for hosting the VM.

The project demonstrates principles of modularity, reusability, and secure, manageable cloud automation.

---

## What is Terraform? 

Terraform is an Infrastructure as Code (IaC) tool developed by HashiCorp, used for provisioning and managing cloud infrastructure through declarative configuration files.

### Benefits of Terraform:

- **Declarative approach:** you define what should exist, not how to create it.
- **Idempotency:** running terraform apply multiple times won’t recreate resources if nothing has changed.
- **Module support:** easily reuse configuration blocks and break your infrastructure into logical, maintainable parts.
- **Multi-cloud support:** works with Yandex Cloud, AWS, GCP, Azure, and many other providers.
- **Version control friendly:** configurations can be stored in Git and tracked like any other code.
- **CI/CD automation:** Terraform integrates smoothly with DevOps pipelines such as GitHub Actions, GitLab CI, and others.


---

## Structure of the project

```
Terraform/
├── main.tf                  # Main logic: VM, networking, and S3 module connection
├── provider.tf              # Yandex.Cloud provider configuration
├── variables.tf             # Declaration of input variables
├── terraform.tfvars         # Variable values (e.g., cloud_id, folder_id, service account key)
├── sa-key.json              # Service account key (used for Terraform authentication)
├── cloud-init.yaml          # Cloud-init script to configure the VM on first boot
├── terraform.tfstate        # Terraform state file (auto-generated)
├── terraform.tfstate.backup # Backup of the previous state (auto-generated)
├── tfplan                   # Terraform plan file (can be generated manually)
├── nametest                 # Optional test file (if used)
├── README.md                # Project instructions (can be extended)
└── modules/
    └── s3/                  # Reusable module for creating the Object Storage (S3 bucket)
        ├── main.tf
        ├── outputs.tf
        ├── variables.tf
        └── versions.tf

```

## 🛠️ How To Run

1. **Initialize Terraform**:  

```
terraform init
```

2. **Plan the changes**:

``` 
terraform plan
```

3. **Apply the changes**:  

```
terraform apply
```

4. **The VM is configured automatically**:  
   The cloud-init.yaml script installs AWS CLI, sets up credentials, and uploads a file to the S3 bucket.

As a result:
- Resources are created in Yandex Cloud.

- The VM is auto-configured and gains access to the S3 bucket.

- Everything is managed and tracked through Terraform.

---
## Examples of work: 
<img width="1388" alt="Screenshot 2025-05-22 at 11 20 52 PM" src="https://github.com/user-attachments/assets/ba202dbe-4d5c-4a31-be14-703147233ac1" />

<img width="1394" alt="Screenshot 2025-05-22 at 11 22 11 PM" src="https://github.com/user-attachments/assets/1f4ddb5c-a0b5-4f36-b665-544a62dc2a2d" />


---

## Requirements

- Terraform
- Account in Yandex Cloud
- Service accound with roles
