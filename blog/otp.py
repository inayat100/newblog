import os
from twilio.rest import Client

account_sid = os.environ['AC84918ceed15f4751c6863a53e429d28e']
auth_token = os.environ['c922625f33f151ab14cdff2471d524b4']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="opt is 243725",
                     from_='+17175002897',
                     to='+917078711121'
                 )