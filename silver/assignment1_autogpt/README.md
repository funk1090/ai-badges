# Silver Assignment 1 — AutoGPT Demo

This assignment demonstrates the installation and execution of AutoGPT inside a WSL environment. The goal is to show that the student can install dependencies, configure the environment, run AutoGPT, and execute a simple goal using an OpenAI API key.

## 1. Environment Setup (WSL)

The following commands were executed on a fresh WSL Ubuntu environment:

```bash
wsl --install
sudo apt update
sudo apt install python3 python3-pip git curl -y
