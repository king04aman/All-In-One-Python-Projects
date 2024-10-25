# Base Image
FROM python:3.10

# Working directory
WORKDIR /app

# Code
COPY . .

# Install Libraries
RUN pip install -r requirement.txt

# run app
CMD ["python", "main.py"]

