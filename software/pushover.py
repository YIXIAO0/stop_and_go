import requests

class Pushover:
    def __init__(self):
        self.USER_ID = 'gaq7tp7pgptony4xe2yg12r49zry8x'
        self.API_KEY = 'a9kidboenzcynzqwe8m7imsrkorh2u'

    def send_message(self, text):
        payload = {'message': text, 'user': self.USER_ID, 'token': self.API_KEY }
        r = requests.post('https://api.pushover.net/1/messages.json', data=payload, headers={'User-Agent': 'Python'})
        return r


def example():
    pushover = Pushover()
    pushover.send_message("be careful!")
    
if __name__ == "__main__":
    example()