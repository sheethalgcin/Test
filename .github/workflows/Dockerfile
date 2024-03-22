
# Use a base image with Linux environment
FROM ubuntu:latest

# Install other tools or dependencies as needed
RUN apt-get update && \
    apt-get install -y curl wget git && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 16.20.2

# Install NVM
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Install Node.js and npm using NVM
RUN export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install $NODE_VERSION && \
    nvm use $NODE_VERSION && \
    npm install -g npm@8.5.5 && \
    npm cache clean --force

# Add NVM to PATH
ENV PATH $NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH

# Check node and npm version
RUN node -v && npm -v

# Set working directory
WORKDIR /workspace

# Copy files into workspace
COPY * ./

# Optionally, continue with the rest of your Dockerfile instructions


