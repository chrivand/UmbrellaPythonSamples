# import necessary libraries / modules
import requests
import json
from datetime import datetime
import base64

# API key and secret, combined, base64 encoded and decoded
API_key = "<your_key>"
API_secret = "<your_secret>"
API_combined = API_key + ":" + API_secret
base64 = (base64.standard_b64encode(bytes(API_combined, 'utf-8'))).decode("utf-8")

# enter organizational ID here
organization = "<your_org>"

# URL needed for the security activity
reporting_url = "https://reports.api.umbrella.com/v1/organizations/" + organization + "/security-activity"

# time for timestamp of verdict domain
time = datetime.now().isoformat()

#create header for authentication
headers = {
    'Authorization': "Basic " + base64
    }

# do GET request for the domain status and category
req = requests.get(reporting_url, headers=headers)

output = req.json()

if(req.status_code == 200):
	print("SUCCESS at %(time)s: this is the most recent security activity: %(output)s" % {'time': time, 'output': output})
else:
	print("An error has ocurred with the following code %(error)s, please consult the following link: https://docs.umbrella.com/investigate-api/" % {'error': req.status_code})
