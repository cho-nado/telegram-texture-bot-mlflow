# Telegram texture bot with mlflow

## What This Project Is?
A Telegram bot that recognizes image textures using a fine-tuned ResNet-50 model. Users send a photo via Telegram, and the bot replies with a predicted texture class (from 47 DTD categories) and its confidence score.

---
## What Is Implemented

### Model loading & inference:
- PyTorch ResNet-50, last FC layer replaced for 47 classes.
- Pretrained on DTD weights (resnet50_dtd_split1.pth).

### Telegram bot:
- /start command and “screen” button.
- Photo handler downloads the image, preprocesses, runs inference, and replies.

### MLflow integration:
- Each inference run is logged as an MLflow run.
- Logs include parameters (predicted_class), metrics (confidence), and the input image as an artifact.

### Docker & Docker Compose:
- Two containers: bot and MLflow UI.
- Shared volume ./mlruns for storing experiment data.

---

## Project Structure

```bash
.
├── TBot_resnet50.py         # Main bot + inference + MLflow logging
├── requirements.txt         # Python dependencies (torch, mlflow, python-telegram-bot, etc.)
├── Dockerfile               # Builds the Telegram-bot container
├── mlflow.Dockerfile        # Builds the MLflow-UI container
├── docker-compose.yml       # Orchestrates both services and shared volume
└── mlruns/                  # Volume for MLflow experiment logs & artifacts
```
---
## Technologies used:
- Python, PyTorch, ResNet50
- Telegram Bot API
- Docker, Docker Compose
- MLflow for experiment tracking

---
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

---
## Where to Analyze Results
- MLflow UI (http://localhost:8001) lists all inference runs.
- Compare multiple runs side-by-side to see confidence distributions or class frequencies.

---
## What You Can Analyze via MLflow UI

- **Run comparisons:** visualize confidence metrics across different images.

- **Artifact inspection:** review the exact input that produced each prediction.

- **Filtering & search:** find runs by class name or confidence threshold.

- **Reproducibility:** every inference is logged with exact code & environment versions.


--- 
## Why All This?
- **Experiment tracking** ensures every prediction is recorded—no more “I forgot what parameters I used.”

- **Reproducibility:** you can roll back to any run and re-inspect inputs.

- **Scalability:** laying this MLOps foundation lets you later add training runs, hyperparameter sweeps, model registry, etc.

---
## Why Use MLflow for a Small Project?

- Even simple inference projects benefit from **structured logging**—you’ll never lose track of which images gave low confidence or unexpected classes.

- **Demonstrates best practices** in MLOps, making your work more professional and ready for team collaboration.

- **Low overhead:** once set up, logging happens automatically and gives you powerful UI tools for free.









