from slackclient import SlackClient

# token obtained from
# https://api.slack.com/custom-integrations/legacy-tokens
slack_token = '<obtained from link in comment above>'
kevin = 'DA2CGFVBJ' # I dont know how to find this with code
notify = 'notifications' # channel for notifications

slack_client = SlackClient(slack_token)

def list_private_channels():
    channels_call = slack_client.api_call("group.list") 
    if channels_call['ok']: 
        return channels_call['groups'] 
    return None
 
def list_channels(): 
    channels_call = slack_client.api_call("channels.list") 
    if channels_call['ok']: 
        return channels_call['channels'] 
    return None

def channel_info(channel_id): 
    ch_info = slack_client.api_call("channels.info", channel=channel_id) 
    if ch_info: 
        return ch_info['channels'] 
    return None

def send_message(channel_id, message): 
    slack_client.api_call( 
        "chat.postMessage", 
        channel=channel_id, 
        text=message, 
        username='Cardboard Box', 
)

def print_channels():
    channels = list_channels() 
    for channel in channels: 
        print('Channel: {} ({}), Members: {}, Creator: {}'.format(channel['name'], channel['id'], channel['members'], channel['creator']))

send_message(notify,'testing')

# channels = channels_call['channels']
# members = channels[0]['members'] # a list
# slackbot = channels[0]['creator']
# kevin = members[0]



