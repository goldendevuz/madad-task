FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_LINK_MODE=copy

WORKDIR /usr/src/app

# Install system dependencies and ngrok
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl make sudo ca-certificates gnupg && \
    curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
    | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
    echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
    | sudo tee /etc/apt/sources.list.d/ngrok.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends ngrok && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install jprq (cached if install.sh doesn't change)
RUN curl -fsSL https://jprq.io/install.sh | sudo bash

# Download and install uv with explicit caching of the tarball
RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-musl.tar.gz -o uv.tar.gz && \
    tar -xzvf uv.tar.gz && \
    mv uv-x86_64-unknown-linux-musl/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv && \
    rm -rf uv-x86_64-unknown-linux-musl uv.tar.gz

# Upgrade pip early, so if requirements.txt hasn't changed, this layer caches well
RUN pip install --upgrade pip

# Copy only requirements first to leverage Docker cache if code changes but deps don't
COPY requirements.txt .

# Install python dependencies from requirements.txt (cached if requirements.txt unchanged)
RUN uv init
RUN uv add -r requirements.txt

# Now copy the rest of the project files
COPY . .

# Expose the port your app listens on
EXPOSE 1024

# Default command to start your app
CMD ["bash", "start.sh"]
