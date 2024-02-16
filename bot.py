import fortnitepy
import json
import os

OPENAI_API_KEY='key'

from openai import OpenAI
aiclient = OpenAI(api_key=OPENAI_API_KEY)




code = input("auth code: ")

class MyClient(fortnitepy.Client):
    def __init__(self):
        device_auth_details = self.get_device_auth_details().get(email, {})
        super().__init__(
            auth=fortnitepy.AuthorizationCodeAuth(code)
        )

    def get_device_auth_details(self):
        if os.path.isfile(filename):
            with open(filename, 'r') as fp:
                return json.load(fp)
        return {}

    def store_device_auth_details(self, email, details):
        existing = self.get_device_auth_details()
        existing[email] = details

        with open(filename, 'w') as fp:
            json.dump(existing, fp)

    async def event_device_auth_generate(self, details, email):
        self.store_device_auth_details(email, details)

    async def event_ready(self):
        print('----------------')
        print('Client ready as')
        print(self.user.display_name)
        print(self.user.id)
        print('----------------')
         # Get the party instance
        party = client.party

        # Set party privacy to public
        await party.set_privacy(fortnitepy.PartyPrivacy.PUBLIC)
    


    
   
    async def event_party_invite(self, request):
        await request.accept()

    async def event_friend_message(self, message):
        print('Received message from {0.author.display_name} | Content: "{0.content}"'.format(message))
        completion = aiclient.chat.completions.create(
             model="gpt-3.5-turbo",
             messages=[
                {"role": "system", "content": "You are a friendly Fortnite players. You are there to chat to - and assist - other Fortnite players! You can talk in all lowercase and use some gen z slang. "},
                {"role": "user", "content": message.content}
            ]
        )

        message.reply(completion.choices[0].message)           




client = MyClient()
client.run()
