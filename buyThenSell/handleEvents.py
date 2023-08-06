import _global

def handleEvent(data):
    if data['event'] == 'auth':
        if data['status'] == 'OK':
            print('API authentication successful')

    elif data['event'] == 'subscribed':
        if data['channel'] == 'ticker':
            _global.channels[data['chanId']] = [data['channel'], data['pair']]