from twilio.rest import Client

# ✅ Your Twilio credentials
ACCOUNT_SID = "<YOUR_ACCOUNT_SID>"
AUTH_TOKEN = "<YOUR_AUTH_TOKEN>"
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Replace with your approved WhatsApp business number
whatsapp_from = "whatsapp:+919967640968"   # Example; replace with your Twilio WhatsApp-enabled number
# Replace with your personal WhatsApp number
whatsapp_to = "whatsapp:+919810890461"
customer_name = "Anurag Mishra"
order_id = "123456"
# Use an approved template (check Twilio Console > Messaging > WhatsApp Templates)
try:
    message = client.messages.create(
        from_=whatsapp_from,
        to=whatsapp_to,
        body=f"Hello {customer_name}, your order #{order_id} is confirmed!"

    )
    print(f"✅ Message sent. SID: {message.sid}")
    print(f"Status: {message.status}")
except Exception as e:
    print("❌ Failed to send:", e)


