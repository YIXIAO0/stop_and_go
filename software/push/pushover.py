import sys
import os
import requests

# USER = os.environ['PUSHOVER_USER_ID']
# API = os.environ['PUSHOVER_API_TOKEN']
# USER = 'uogjxyo7s99rtqbg3c3dustyis3ee3' # user key
USER = 'gaq7tp7pgptony4xe2yg12r49zry8x'
API = 'a9kidboenzcynzqwe8m7imsrkorh2u'

def send_message(text):
    payload = {"message": text, "user": USER, "token": API }
    r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
    return r
    
def main():
    r = send_message(" ".join(sys.argv[1:]))
    if not r.status_code == 200:
        print(r.text)
    
if __name__ == '__main__':
    main()
