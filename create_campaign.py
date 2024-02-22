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


configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = os.getenv('API_KEY')
# Instantiate the client\
# sib_api_v3_sdk.configuration.api_key = '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'

api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
tag = 'myTag'
sender = {"name": 'Derex', "email": 'derexfinesse@gmail.com'}
name = 'My First Campaign'
template_id= 45
scheduled_at = "2024-02-21 04:50:01"
subject = ' My Subject'
reply_to = 'replyto@domain.com'
to_field = 'derexfinesse@gmail.com'
recipients = {"listIds": [30, 30], "exclusionListIds": [2]}
attachment_url = 'https://attachment.domain.com/myAttachmentFromUrl.jpg'
inline_image_activation = False
mirror_active = False
header = 'If you are not able to see this mail, click {here}'
footer = 'If you wish to unsubscribe from our newsletter, click {here}'
utm_campaign = 'My utm campaign value'
email_campaigns = sib_api_v3_sdk.CreateEmailCampaign(tag=tag, sender=sender, name=name, template_id=template_id, scheduled_at=scheduled_at, subject=subject, reply_to=reply_to, to_field=to_field, recipients=recipients, attachment_url=attachment_url, inline_image_activation=inline_image_activation,mirror_active=mirror_active, header=header, footer=footer, utm_campaign=utm_campaign) # CreateEmailCampaign | Values to create a campaign

try:
    api_response = api_instance.create_email_campaign(email_campaigns)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->create_email_campaign: %s\n" % e)