# Install Python3 on Nix

## Install on Ubuntu

### Setting Up Python 3
```
sudo apt update && sudo apt -y upgrade
```
Make sure, all the following pkgs installed on your machine:
```
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```
After process completed, check the installed version of python3:
```
python3 -V
```
then install pip:
```
sudo apt install -y python3-pip
```

### Setting Up a Virtual Environment

Virtual environments enable you to have an isolated space on your server for Python projects.

The install steps are:
```
sudo apt install -y python3-venv
mkdir environments && cd environments

python3 -m venv my_env
ls my_env
```

To use this environment, you need to activate it:
```
source my_env/bin/activate
```


## Install on MacBook

Install Homebrew on Mac:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Install pyenv to Manage Your Python Versions:
```
brew install pyenv
```
Use pyenv to Install Python or Update Your Python Version:
```
pyenv install 3.9.2 
```