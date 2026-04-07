# Use a Python image with PyTorch pre-installed to save time
FROM pytorch/pytorch:latest

WORKDIR /app
COPY . /app

# Install FastAPI and Uvicorn for the server logic
RUN pip install fastapi uvicorn torchvision transformers openai

# OpenEnv usually communicates on port 8000
EXPOSE 8000

CMD ["python", "inference.py"]