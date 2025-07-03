#!/bin/bash

# This script is for running Ultroid on Google Colab.

# Install telethonpatch first
pip install https://github.com/New-dev0/Telethon-Patch/archive/main.zip

# 1. Clone the repository
git clone https://github.com/op30mmd/Ultroid
cd Ultroid

# 2. Create a .env file
# You will need to fill in your own values for these variables.
cp .env.sample .env

# 3. Run the bot
python3 -m pyUltroid