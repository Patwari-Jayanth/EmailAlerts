from google.oauth2 import service_account
from googleapiclient.discovery import build
from twilio.rest import Client
from googleapiclient.errors import HttpError

# Set up Twilio credentials (replace with your own credentials)
twilio_account_sid = 'ACd0c169355a1920794636cc615f3ba771'
twilio_auth_token = 'df1e4dc2583c6070a3abcc7929fcf9cb'
twilio_phone_number = '+13072714045'
your_phone_number = '+919652011747'  # Format: +1234567890

# Initialize Gmail API using OAuth2 credentials
def initialize_gmail_api(credentials_file):
    scopes = ['https://www.googleapis.com/auth/gmail.readonly']
    creds = service_account.Credentials.from_service_account_file(
        credentials_file, scopes=scopes)
    service = build('gmail', 'v1', credentials=creds)
    return service

# Check for new emails from a specific sender
def check_for_new_email(service, sender_email):
    try:
        results = service.users().messages().list(userId='me', q=f'from:{sender_email} is:unread').execute()
        messages = results.get('messages', [])
        return messages
    except HttpError as e:
        print(f'Gmail API error: {e}')
        return []

# Send a WhatsApp message using Twilio
def send_whatsapp_message(message_body):
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(
        from_=twilio_phone_number,
        body=message_body,
        to=your_phone_number
    )

if __name__ == '__main':
    try:
        credentials_file = 'C:/Users/Dell/Downloads/gmail-alert-404213-0be02655ad0a.json'
        service = initialize_gmail_api(credentials_file)
        sender_email = 'peddykarthik1027@gmail.com'
        messages = check_for_new_email(service, sender_email)
        send_whatsapp_message("hello-6940")
        if messages:
            for message in messages:
                send_whatsapp_message(f'hey hiii , 6939 ..You have a new email from {sender_email}: https://mail.google.com/mail/u/0/#inbox/{message["id"]}')
    
    except Exception as e:
        print(f'An error occurred: {e}')
