#!/bin/bash

if ! command -v ollama > /dev/null
then
    echo "'ollama' is not installed. Installing it now..."
    curl -fsSL https://ollama.com/install.sh | sh
else
  echo "'ollama' is installed."
fi

echo "Pulling the model 'qwen2.5-coder:1.5b-instruct-q5_K_M'..."
ollama pull qwen2.5-coder:1.5b-instruct-q5_K_M

echo "Installing 'llsh' from TestPyPI..."
pip install -i https://test.pypi.org/simple/ llsh

if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
else
    echo "This script only works under Bash or Zsh :("
    exit 1
fi
LLX_ALIAS="alias llx='function _llx() { eval \$(llsh \"\$@\"); }; _llx'"
# Check if the alias already exists in .zshrc
if ! grep -q "alias llx=" "$SHELL_RC"; then
    echo "Adding alias 'llx' to $SHELL_RC..."
    echo "$LLX_ALIAS" >> "$SHELL_RC"
    echo "To use 'llx', run 'source ~/.zshrc' or restart your terminal."
else
  echo "'llx' is already installed."
fi

echo "Installation complete!"
