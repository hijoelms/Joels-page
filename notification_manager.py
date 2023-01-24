from twilio.rest import Client
import os


class NotificationManager:

    def __init__(self,TWILIO_SID,TWILIO_AUTH_TOKEN ):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self,virtual_number,verified_number, message):
        message = self.client.messages.create(
            body=message,
            from_=virtual_number,
            to=verified_number,
        )
        # Prints if successfully sent.
        print(message.sid)
