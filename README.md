# termux-ip-tracker
# STEP 1: Install Termux and open it

# STEP 2: Install required packages
$ pkg update && pkg upgrade -y
$ pkg install git python -y

# STEP 3: Clone the IP tracker
$ git clone https://github.com/YOUR-USERNAME/termux-ip-tracker.git
$ cd termux-ip-tracker

# STEP 4: Install Python dependencies
$ pip install requests

# STEP 5: Run the script
$ python iptracker.py
