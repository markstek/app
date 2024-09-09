import random
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
SCOPES = ['https://mail.google.com/']
def get_random_credentials():
    securities_folder = 'credentials'
    credentials_files = [f for f in os.listdir(
        securities_folder) if f.endswith('.json')]
    if not credentials_files:
        raise Exception("No credentials files found in the Securities folder.")
    selected_file = random.choice(credentials_files)
    creds_path = os.path.join(securities_folder, selected_file)
    return creds_path, selected_file


def get_profile_picture_with_update_time():
    creds_path, selected_file = get_random_credentials()
    token_path = f'credentials\\Tokens\\token_{selected_file}'
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    service = build('people', 'v1', credentials=creds)
    return "Done"


get_profile_picture_with_update_time()