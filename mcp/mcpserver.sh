#!/bin/bash
source /root/.local/bin/env
sleep 1
export OLLAMA_HOST=ollama:11434
/root/go/bin/mcphost -m ollama:llama3.2:latest --config config.json