This will scan your network every 30 seconds, which you can change the interval time. When the program detects a device that has joined the network (either new device or a devide rejoining), this will send you a message via telegram.

first run - pip install python-telegram-bot scapy

change the following in the py file:
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN" - loose example "2356345:wj5gojw5goi4j5igjeo5ijeoi"
chat_id='YOUR_TELEGRAM_CHAT_ID' - loose example '37534753'
pdst="192.168.1.1/24" - change to your own network


for Token, generate one by creating new bot on Telegram with BotFather
for chat_id, you can message a GetMyID bot, and they will reply with your chat id
