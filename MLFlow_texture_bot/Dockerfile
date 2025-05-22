FROM python:3.10.12
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY TBot_resnet50.py resnet50_dtd_split1.pth ./

CMD ["python3", "TBot_resnet50.py"]
