import wit
import json
import subprocess

access_token = 'YOUR TOKEN'
wit.init()

while(True):
    jsonResponse = wit.voice_query_auto(access_token)
    print('Response: {}'.format(jsonResponse))
    if not jsonResponse:
        continue;
    dataDict = json.loads(jsonResponse)
    try:
        if (dataDict["outcomes"][0]["intent"] == "turn_off_lights"):
            subprocess.call(['/home/pi/scripts/lightswitch','off'])
        elif (dataDict["outcomes"][0]["intent"] == "turn_on_lights"):
            subprocess.call(['/home/pi/scripts/lightswitch','on'])
    except (KeyError, IndexError) as e:
        print("Intent not detected")
wit.close()
