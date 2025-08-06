#!/bin/bash
# curl -sSL https://raw.githubusercontent.com/youruser/yourrepo/main/install.sh | bash

set -e  # stop on error

echo "🔧 Updating system..."
sudo apt update && sudo apt upgrade -y

echo "📦 Installing essentials..."
sudo apt install -y git curl wget build-essential zsh unzip

echo "🐍 Installing Python & pip..."
sudo apt install -y python3 python3-pip


echo "⚙️ Setting Zsh as default shell..."
if [ "$SHELL" != "$(which zsh)" ]; then
  chsh -s "$(which zsh)" "$USER"
  echo "✅ Zsh set as default shell. Please log out and log back in."
else
  echo "ℹ️ Zsh is already the default shell."
fi

echo "🧪 Installing Oh My Zsh..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

