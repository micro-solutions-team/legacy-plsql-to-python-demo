FROM python:3.11-slim

WORKDIR /app

# Copy requirements from the local app folder to the container workdir
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FIX: Copy the local 'app' folder INTO a folder named 'app' in the container
COPY app/ ./app/

# FIX: Now uvicorn can find the 'app' module correctly
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]