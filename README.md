# termux-ip-tracker
# STEP 1: Install Termux and open it

# Install required packages
$ pkg update && pkg upgrade -y

$ pkg install git python -y

# Clone the IP tracker
$ git clone https://github.com/itsjust-Rex/termux-ip-tracker.git

$ cd termux-ip-tracker

# Install Python dependencies

$ pip install requests

# Run the script with 👇👇

$ python iptracker.py
