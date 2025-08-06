
# N8N
nvm use v22.16.0
n8n start

# Conda
conda create -n agent python=3.11 -y
conda activate agent

# freezing all requiremens and installing them
pip freeze > requirements.txt
pip install -r requirements.txt

# Vaults 
our obsidian vaults are now here
 