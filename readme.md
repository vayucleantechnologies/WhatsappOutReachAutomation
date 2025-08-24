# WhatsApp Outreach Automation

## 📖 Overview

This project automates sending personalized WhatsApp messages to a list of contacts using the Twilio API. It preprocesses a CSV file containing contact details, sends messages using an approved template, and updates the delivery status in the dataset.

---

## 🚀 Features

1. **CSV Preprocessing**:
   - Normalizes phone numbers (e.g., adds country code if missing).
   - Handles multiple numbers in a single row by duplicating rows.

2. **Automated Messaging**:
   - Sends personalized WhatsApp messages using Twilio's approved templates.
   - Attaches a PDF file to the message.

3. **Delivery Status Tracking**:
   - Updates the "SENT" column in the dataset with the delivery status.

---

## 🛠️ Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Twilio
- Sign up for a [Twilio account](https://www.twilio.com/).
- Get your **Account SID**, **Auth Token**, and **Template SID**.
- Replace the placeholders in [`main.py`](main.py) with your Twilio credentials:
  ```python
  account_sid = "<YOUR_ACCOUNT_SID>"
  auth_token = "<YOUR_AUTH_TOKEN>"
  TEMPLATE_SID = "<YOUR_TEMPLATE_SID>"
  ```

### 4. Prepare the Dataset
- Place your raw dataset in `resources/data.csv`.
- Ensure the CSV has the following columns:
  ```
  Company Name, Name, Designation, Email, Website, Number, Address, SENT
  ```

---

## 📂 Project Structure

```
.
├── .gitignore               # Files to ignore in version control
├── main.py                  # Main script for automation
├── test.py                  # Test script for Twilio integration
├── requirements.txt         # Python dependencies
├── recoveryCode.txt         # Recovery codes (example file)
├── notes.txt                # Message template
├── resources/               # Directory for resources
│   ├── data.csv             # Raw dataset
│   └── data_clean.csv       # Preprocessed dataset
├── logs/                    # Directory for logs
│   └── whatsapp.log         # Log file
```

---

## 📝 Usage

### 1. Preprocess the Dataset
Run the script to preprocess the dataset:
```bash
python main.py
```
This will:
- Normalize phone numbers.
- Save the cleaned dataset to `resources/data_clean.csv`.

### 2. Send WhatsApp Messages
The script will:
- Read the cleaned dataset.
- Send personalized messages to each contact.
- Update the "SENT" column with the delivery status.

### 3. Check Logs
Logs are saved in the `logs/whatsapp.log` file for debugging and tracking.

---

## 📧 Message Template

The message template is defined in [`notes.txt`](notes.txt). It uses placeholders like `{{1}}` for dynamic content (e.g., recipient's name).

---

## ⚠️ Important Notes

1. **Twilio Sandbox**:
   - If using the Twilio sandbox, ensure the recipient has joined your sandbox by sending a message to the Twilio-provided number.

2. **Rate Limiting**:
   - The script includes a 2-second delay between messages to avoid rate limiting.

3. **PDF Attachment**:
   - The PDF file is hosted online. Update the `PDF_LINK` variable in [`main.py`](main.py) with your file's direct URL.

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.

---

## 📞 Contact

For any inquiries, please contact:
- **Email**: info@vayucleantechnologies.com
- **Phone**: +91 89835 74406