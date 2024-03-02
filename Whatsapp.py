import pywhatkit as kit

# Replace 'recipient_phone_number' with the recipient's phone number, including the country code (e.g., +1 for the United States)
recipient_phone_number = "+..........."

# Replace 'your_message' with the message you want to send
message = "Hello, this is an automated WhatsApp message sent from Python!"

# Specify the time in 24-hour format when you want to send the message
# Replace 'send_hour' and 'send_minute' with the desired time
send_hour = 21  # 2:00 PM
send_minute = 00

# Send the message
kit.sendwhatmsg(recipient_phone_number, message, send_hour, send_minute)
