# telegram-texture-bot-mlflow

Telegram bot for texture recognition using ResNet50, Docker, and MLflow.

# Telegram Texture Recognition Bot 🖼️

A Telegram bot that classifies image textures using a ResNet50 neural network. The bot is containerized with Docker and logs experiments using MLflow.

## Technologies used:
- Python, PyTorch, ResNet50
- Telegram Bot API
- Docker, Docker Compose
- MLflow for experiment tracking

## Usage 🛠️

1. Clone the repository:

```bash
git clone https://github.com/cho-nado/telegram-texture-bot-mlflow
cd telegram-texture-bot-mlflow
```

2. Export your Telegram token:

```bash
export TELEGRAM_TOKEN_TEXTURE='YOUR_TELEGRAM_TOKEN'
```

3. Run Docker Compose:

```bash
docker-compose build
docker-compose up
```
4. Open MLflow UI at:

```bash
http://localhost:8001
``` 
