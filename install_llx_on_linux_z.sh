#!/bin/zsh

if ! command -v ollama &> /dev/null
then
    echo "'ollama' is not installed. Installing it now..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

echo "Pulling the model 'qwen2.5-coder:1.5b-instruct-q5_K_M'..."
ollama pull qwen2.5-coder:1.5b-instruct-q5_K_M

echo "Installing 'llsh' from TestPyPI..."
pip install -i https://test.pypi.org/simple/ llsh

ZSHRC_FILE="$HOME/.zshrc"
LLX_ALIAS="alias llx='function _llx() { eval \$(llsh \"\$@\"); }; _llx'"
# Check if the alias already exists in .zshrc
if ! grep -q "alias llx=" "$ZSHRC_FILE"; then
    echo "Adding alias 'llx' to $ZSHRC_FILE..."
    echo "$LLX_ALIAS" >> "$ZSHRC_FILE"
    echo "To use 'llx', run 'source ~/.zshrc' or restart your terminal."
fi

echo "Installation complete!"