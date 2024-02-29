from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR API KEY'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
template_id = 1
email_to = ["example1@example1.com","example2@example2.com"]
send_test_email = sib_api_v3_sdk.SendTestEmail(email_to=email_to)

try:
    api_instance.send_test_template(template_id, send_test_email)
except ApiException as e:
    print("Exception when calling SMTPApi->send_test_template: %s\n" % e)