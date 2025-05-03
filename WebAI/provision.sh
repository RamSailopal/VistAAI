#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
apt update
apt install -y python3 ttyd python3-argparse-addons python3-termcolor python3-requests
cd /home/WebAI
ttyd -p 8001 -W python3 appcmd.py -s ollama:11434