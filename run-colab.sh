#!/bin/bash

# This script is for running Ultroid on Google Colab.

# Remove existing Ultroid directory if it exists
rm -rf Ultroid

# 1. Clone the repository
git clone https://github.com/op30mmd/Ultroid
cd Ultroid

# 2. Install dependencies
pip install https://github.com/New-dev0/Telethon-Patch/archive/main.zip
pip install -r requirements.txt

# 3. Create and populate .env file with placeholders
cp .env.sample .env
sed -i 's/^API_ID=$/API_ID=6/' .env
sed -i 's/^API_HASH=$/API_HASH=YOUR_API_HASH/' .env
sed -i 's/^SESSION=$/SESSION=YOUR_STRING_SESSION/' .env
sed -i 's/^LOG_CHANNEL=$/LOG_CHANNEL=0/' .env

echo "======================================================================"
echo "IMPORTANT: Please edit the .env file with your actual API_ID, API_HASH, and SESSION."
echo "LOG_CHANNEL has been set to 0 by default. Update if needed."
echo "You can find the .env file in the 'Ultroid' directory."
echo "======================================================================"

# 4. Run the bot
python3 -m pyUltroid