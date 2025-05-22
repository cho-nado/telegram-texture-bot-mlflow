# Telegram Texture Bot + Terraform Infrastructure

This repository contains two projects:

---

## 📦 `MLFlow_texture_bot`

The project includes:

- A Telegram bot for classifying image textures;

- An MLflow server for experiment logging;

- A plan for integrating CI/CD and automating model tracking.

---
### 🛠️ How to Run

1. Install dependencies (using requirements.txt or pip install).

2. Start the Telegram bot, providing the token and the model path (see project docs for exact instructions).

3. The bot will accept images, predict their texture class, and log the results to MLflow.

---
## Why MLflow? 
**(check details in the project)**

MLflow enables you to:

- Track all experiments (model versions, metrics, dates);

- Reproduce training runs with the same parameters;

- Centrally manage model versions.

---

## ☁️ Terraform

This configuration deploys infrastructure on Yandex Cloud, including:

- An S3 bucket (Object Storage) for file storage;

- A virtual machine that automatically uploads a file to the bucket via cloud-init;

- A network and subnet for the VM.

---
### 🛠️  How to Run

```bash
cd Terraform
terraform init
terraform apply
```

After deployment:

- A bucket will appear in Yandex.Cloud (e.g., ilartstu-mlflow);

- The VM will upload the file test.txt to it.

To tear down:

```bash
terraform destroy

```

---
## 🚀 CI/CD Pipeline

To ensure code quality and reliable infrastructure changes, this project uses a **CI/CD** pipeline powered by **GitHub Actions**. Every time you push to `main` or open a pull request, the workflow automatically:

1. **Checks out** the repository  
2. **Sets up Python 3.10**  
3. **Installs and verifies** Python dependencies (`requirements.txt` + `mlflow`)  
4. **Builds the Docker image** for the Telegram texture bot  
5. **Initializes, validates & plans** Terraform configuration  

This gives us instant feedback if:
- Any Python dependency is broken  
- The Dockerfile has syntax errors  
- The Terraform code contains misconfigurations  

<img width="1478" alt="Screenshot 2025-05-23 at 12 21 38 AM" src="https://github.com/user-attachments/assets/25438ab3-4021-4544-91b7-de105b1791d2" />


By automating these steps, we catch issues early, maintain reproducibility, and guarantee that both the application and its infrastructure are always in a deployable state.  





