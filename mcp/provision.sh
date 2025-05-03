#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt update
apt install -y curl wget python3-requests
curl -LsSf https://astral.sh/uv/install.sh | sh
source /root/.local/bin/env
cd /tmp
wget https://go.dev/dl/go1.24.2.linux-amd64.tar.gz
tar -xvf go1.24.2.linux-amd64.tar.gz -C /usr/local
/usr/local/go/bin/go install github.com/mark3labs/mcphost@latest
cd /home/mcp
uv init
uv add requests
export OLLAMA_HOST=ollama
#/root/go/bin/mcphost -m ollama:llama3.2:latest --config config.json
tail -f /dev/null
