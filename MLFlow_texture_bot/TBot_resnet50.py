# TBot_resnet50.py
import logging
import os

import mlflow
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image

import nest_asyncio  
nest_asyncio.apply()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)

# ---------------------
# MLflow config
# ---------------------
# хранилище в папке ./mlruns
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://mlflow:5000"))

mlflow.set_experiment("TextureRecognition")

# ---------------------
# LOGGING
# ---------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ---------------------
# GLOBAL VARIABLES
# ---------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

classes = [
    "banded", "blotchy", "braided", "bubbly", "bumpy",
    "chequered", "cobwebbed", "cracked", "crosshatched", "crystalline",
    "dotted", "fibrous", "flecked", "freckled", "frilly",
    "gauzy", "grid", "grooved", "honeycombed", "interlaced",
    "knitted", "lacelike", "lined", "marbled", "matted",
    "meshed", "paisley", "perforated", "pitted", "pleated",
    "polka-dotted", "porous", "potholed", "scaly", "smeared",
    "spiralled", "sprinkled", "stained", "stratified", "striped",
    "studded", "swirly", "veined", "waffled", "woven",
    "wrinkled", "zigzagged"
]
num_classes = len(classes)

# ---------------------
# MODEL LOADING
# ---------------------
model = models.resnet50(pretrained=True)
in_features = model.fc.in_features
model.fc = nn.Linear(in_features, num_classes)

weights_path = "resnet50_dtd_split1.pth"
if os.path.exists(weights_path):
    model.load_state_dict(torch.load(weights_path, map_location=device))
    logger.info("Model weights loaded successfully.")
else:
    logger.warning(f"Could not find the weights file {weights_path}! Continuing without loading...")

model.to(device)
model.eval()

# ---------------------
# IMAGE PREPROCESSING
# ---------------------
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std =[0.229, 0.224, 0.225]),
])

# ---------------------
# HANDLERS
# ---------------------
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("screen", callback_data="screen")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Hello! I’m a bot for texture recognition.\n\n"
        "Press the button below to send me an image.",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "screen":
        await query.edit_message_text(
            "Please send me a photo, and I’ll tell you which texture it is."
        )

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]
    image_path = "temp_image.jpg"
    photo_file = await photo.get_file()
    await photo_file.download_to_drive(image_path)

    image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0).to(device)

    with torch.no_grad():
        logits = model(input_tensor)
        probs = F.softmax(logits, dim=1)
        pred_idx = torch.argmax(probs, dim=1).item()
        predicted_class = classes[pred_idx]
        confidence = probs[0, pred_idx].item()

    # логирование инференса в MLflow
    with mlflow.start_run():
        mlflow.log_param("model", "ResNet50_DTD")
        mlflow.log_param("predicted_class", predicted_class)
        mlflow.log_metric("confidence", confidence)
        mlflow.log_artifact(image_path, artifact_path="input_images")

    result_text = f"Predicted class: {predicted_class}\nConfidence: {confidence:.2f}"
    await update.message.reply_text(result_text)

    keyboard = [[InlineKeyboardButton("screen", callback_data="screen")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "If you want to recognize another image, press 'screen'.",
        reply_markup=reply_markup
    )

# ---------------------
# MAIN
# ---------------------
if __name__ == "__main__":
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN_TEXTURE")
    if TELEGRAM_TOKEN is None:
        raise ValueError("TELEGRAM_TOKEN_TEXTURE is not set.")
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    application.run_polling()
