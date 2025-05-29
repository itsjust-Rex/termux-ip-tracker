import requests
import os

def banner():
    os.system('clear')
    print("""
\033[1;32m
  ___ ____    ____            _             
 |_ _|  _ \  |  _ \ ___  __ _| |_ ___  _ __ 
  | || |_) | | |_) / _ \/ _` | __/ _ \| '__|
  | ||  _ <  |  _ <  __/ (_| | || (_) | |   
 |___|_| \_\ |_| \_\___|\__,_|\__\___/|_|   
                                           
         IP Address Tracker
       Created by JUST REX
\033[0m
""")

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()

        print("\n🔍 IP Information:\n")
        for key, value in data.items():
            print(f"{key.capitalize()}: {value}")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    banner()
    target_ip = input("🔎 Enter IP address to track: ")
    get_ip_info(target_ip)
