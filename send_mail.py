from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os


# Load variables from .env file into environment
load_dotenv()

# api_instance = ApiClient()
# api_instance.api_key = {'api-key': os.getenv('API_KEY')}

# Instantiate the client\
sib_api_v3_sdk.configuration.api_key = os.getenv('API_KEY')
api_instance = sib_api_v3_sdk.EmailCampaignsApi()

# Define the scheduled times
scheduled_times = [
    "2024-02-21 04:25:01",  # Example: Scheduled time 1
    "2024-02-21 04:27:01",  # Example: Scheduled time 2
    "2024-02-21 04:28:01"   # Example: Scheduled time 3
]


# Define the campaign settings\
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(
name= "Campaign sent via the API",
subject= "My subject",
sender= { "name": "Derex", "email": "derexfinesse@gmail.com"},
# type= "classic",
# Content that will be sent\
html_content= "Congratulations! You successfully sent this example campaign via the Brevo API.",
# Select the recipients\
recipients= {"listIds": [], "emailAddresses": ["allankiprop175@gmail.com"]},
# Schedule the sending in one hour\
scheduled_at= scheduled_times
)


# Make the call to the client\
try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)