"""
Cisco Cyber Vision API sample script with requests library
Test it now on the DevNet sandbox: https://devnetsandbox.cisco.com
Get the IP address of all components
"""

import requests
import json

center_token = "ics-becf2ba10ba7058ffb9651d69df46e8131090c22-d96b3d752a2899c4c4a0895076e944df49005ccb"
center_ip = "172.16.0.140"
center_port = 443
center_base_url = "api/3.0"

def get_components_ip():
    try:
        headers = { "x-token-id": center_token }
        r_get = requests.get(f"https://{center_ip}:{center_port}/{center_base_url}/components",headers=headers,verify=False)
        r_get.raise_for_status() #if there are any request errors

        #raw JSON data response
        raw_json_data = r_get.json()
        # print(json.dumps(raw_json_data,indent=2))

        # get only the label name and IP address of the component
        components_with_ip_and_label = {}
        for component in raw_json_data:
            components_with_ip_and_label[component["label"]] = component["ip"]

        return components_with_ip_and_label

    except Exception as e:
        return f"Error when connecting: {e}"

all_components = get_components_ip()

print(all_components)
print(json.dumps(all_components,indent = 3))
# print(type(all_components))
