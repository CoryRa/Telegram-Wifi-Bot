from telegram.ext import Updater
from scapy.all import ARP, Ether, srp
import time

# Telegram bot token (replace this with your bot token)
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Dictionary to keep track of devices and their last detection time
devices = {}

# Function to scan the network for new devices
def scan_network():
    while True:
        try:
            # Create ARP packet
            arp_packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="192.168.1.1/24")
            # Send packet and receive responses
            result = srp(arp_packet, timeout=3, verbose=0)[0]
            # Update devices dictionary with new devices
            for sent, received in result:
                if received.psrc not in devices:
                    devices[received.psrc] = time.time()
                    send_telegram_message(f"New device joined the network: {received.psrc}")
            # Remove devices that have not been active for more than 30 seconds
            current_time = time.time()
            devices = {k: v for k, v in devices.items() if current_time - v < 30}
            # Sleep for 30 seconds before scanning again
            time.sleep(30)
        except Exception as e:
            print("Error scanning network:", e)

# Function to send Telegram message
def send_telegram_message(message):
    updater.bot.send_message(chat_id='YOUR_TELEGRAM_CHAT_ID', text=message)

# Main function
def main():
    global updater
    # Create updater for the bot
    updater = Updater(token=TOKEN, use_context=True)
    
    # Start the network scanning
    scan_network()

    # Wait for the bot to be stopped
    updater.idle()


if __name__ == '__main__':
    main()
