"""
Automated WhatsApp Messaging Script with PDF Attachment (via Twilio API)

📌 Description:
1. Preprocesses the CSV:
   - If a row has multiple numbers, duplicates the row so each row has only ONE number.
   - Saves a new normalized dataset before sending.
2. Reads the normalized CSV and sends a personalized WhatsApp message 
   (using approved template) with PDF attachment.
3. Updates the "SENT" column with delivery status.

📝 Dependencies:
- pandas
- twilio
"""

import pandas as pd
from twilio.rest import Client
import json
import time
import os
import logging

# =============== CONFIG ===============
RAW_CSV = "resources/data.csv"          # original raw dataset
NORMALIZED_CSV = "resources/data_clean.csv"   # cleaned dataset
ALLOW_REPEAT = True                      # Toggle: allow resending to "SENT" entries?

TWILIO_WHATSAPP = "whatsapp:+919967640968"   # Twilio sandbox / business number
TEMPLATE_SID = "<YOUR_TEMPLATE_SID>"  # your approved template SID

PDF_LINK = "https://github.com/OPanurag/dummy/blob/main/sample.pdf?raw=true"  # direct link to PDF

# Twilio client (replace with your SID & Token)
account_sid = "<YOUR_ACCOUNT_SID>"
auth_token = "<YOUR_AUTH_TOKEN>"
client = Client(account_sid, auth_token)

# ======================================
def normalize_number(number: str) -> str:
    """Normalize phone number: add +91 if missing, strip spaces."""
    number = number.strip().replace(" ", "")
    if not number.startswith("+"):
        number = "+91" + number
    return number

def preprocess_dataset():
    """Expand dataset so each row has only ONE number."""
    df = pd.read_csv(RAW_CSV)
    new_rows = []

    for _, row in df.iterrows():
        numbers = str(row['Number']).split(",")
        for num in numbers:
            new_row = row.copy()
            new_row['Number'] = normalize_number(num)
            new_rows.append(new_row)

    clean_df = pd.DataFrame(new_rows)
    clean_df.to_csv(NORMALIZED_CSV, index=False)
    logging.info(f"📌 Preprocessed dataset saved to {NORMALIZED_CSV} with {len(clean_df)} rows.")

def send_whatsapp_message(to_number: str, name: str):
    """Send WhatsApp message using approved template with media attachment."""
    return client.messages.create(
        from_=TWILIO_WHATSAPP,
        to=f"whatsapp:{to_number}",
        content_sid=TEMPLATE_SID,
        content_variables=json.dumps({"1": name}),  # {{1}} = Name
        media_url=[PDF_LINK]
    )

def process_contacts():
    """Send messages to all contacts in normalized CSV."""
    if not os.path.exists(NORMALIZED_CSV):
        preprocess_dataset()  # auto-create if not exists

    df = pd.read_csv(NORMALIZED_CSV)

    for idx, row in df.iterrows():
        if not ALLOW_REPEAT and str(row['SENT']).startswith("YES"):
            logging.info(f"⏭️ Skipping {row['Name']} ({row['Company Name']}) - already sent.")
            continue

        try:
            msg = send_whatsapp_message(row['Number'], row['Name'])
            logging.info(f"✅ Sent to {row['Name']} at {row['Number']} (SID: {msg.sid})")
            df.at[idx, 'SENT'] = "YES"
        except Exception as e:
            logging.error(f"❌ Failed for {row['Name']} at {row['Number']}: {e}")
            df.at[idx, 'SENT'] = "FAILED"

        time.sleep(2)  # small delay to avoid rate limiting

    df.to_csv(NORMALIZED_CSV, index=False)
    logging.info("📌 All messages processed. Updated CSV saved.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    preprocess_dataset()  # Step 1: Clean and normalize
    process_contacts()    # Step 2: Send one-by-one
