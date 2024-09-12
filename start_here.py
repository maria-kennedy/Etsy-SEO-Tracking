from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'path_to_your_client_secret.json'
VIEW_ID = 'YOUR_VIEW_ID'

# Authenticate and construct service
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=SCOPES)

analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Request data
response = analytics.reports().batchGet(
    body={
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:sessions'}],
                'dimensions': [{'name': 'ga:sourceMedium'}]
            }]
    }
).execute()

print(response)
