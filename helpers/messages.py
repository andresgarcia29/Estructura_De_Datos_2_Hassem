messages = {
    'error': {
        'rol': '',
        'contract': 'The contract has been broken',
    },
    'success': {
        'rol': '',
        'contract': 'The contract is perfectly'
    }
}


def make_message_to_success(name, action):
    if action == 'create':
        verb = 'created'
    elif action == 'update':
        verb = 'updated'
    elif action == 'delete':
        verb = 'deleted'
    else:
        verb = 'Has no verb'
    return {
        'data': {
            'message': str(name).title() + ' ' + verb
        }
    }


def make_message_to_error(name, action, message):
    if action == 'create':
        verb = 'created'
    elif action == 'update':
        verb = 'updated'
    elif action == 'delete':
        verb = 'deleted'
    else:
        verb = 'Has no verb'
    return {
        'data': {
            'message': str(name).title() + ' ' + verb + ' Error. With code: ' + str(message)
        }
    }
