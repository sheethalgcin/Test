# Use an official Python runtime as a parent image
FROM python:3.x

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

# Copy your test suite files into the container
COPY . /app

# Define the entry point to run Robot Framework
CMD ["python", "--version"]
CMD ["/bin/sh","-c", "robot -d output -o output.xml test.robot"]
