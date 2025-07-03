#!/bin/bash

# This script is for running Ultroid on Google Colab.

# 1. Clone the repository
git clone https://github.com/op30mmd/Ultroid
cd Ultroid

# 2. Install dependencies
pip install https://github.com/New-dev0/Telethon-Patch/archive/main.zip
pip install -r requirements.txt

# 3. Create a .env file
# You will need to fill in your own values for these variables.
cp .env.sample .env

# 4. Run the bot
python3 -m pyUltroid