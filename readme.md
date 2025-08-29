
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
our obsidian vaults are now here. but dont work.

 # adding submodules
 git submodule add https://github.com/anthropics/prompt-eng-interactive-tutorial.git submodules/prompt-eng-interactive-tutorial


 # Notebooks
 start with `jupyter lab`

 #
 if you need to get a repo with your personal

```
git clone git@github-ed25519:santy18/work_workspace
# or
git clone git@github-rsa:KaseyaCodeHub/KaseyaAssistant.git
```


use the different keys like that


# adding ruby kernel
```
\curl -sSL https://get.rvm.io | bash -s stable

source ~/.rvm/scripts/rvm

rvm -v


rvm install ruby --latest
rvm use 3.3.4 --default
ruby -v


gem install bundler
gem install ffi-rzmq
gem install iruby


iruby register --force --user

<!-- verify it works -->
iruby --version
iruby console -e 'puts RUBY_VERSION'
ruby -v
gem list | grep -E 'iruby|ffi-rzmq'

<!-- make sure ruby is there -->
jupyter kernelspec list

<!-- run the kernel -->
jupyter console --kernel ruby

<!-- start the lab -->
jupyter lab

``