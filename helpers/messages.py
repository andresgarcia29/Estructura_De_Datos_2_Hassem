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

def make_message_to_send(name, action, status):
    verb = ''
    if status == 'success':
        status = 'correctly'
    else:
        status = 'with error in the process'
    if action == 'create':
        verb = 'created'
    elif action == 'update':
        verb = 'updated'
    elif action == 'delete':
        verb = 'deleted'
    else:
        verb = 'Has no verb'
    return {
        'message': str(name).title() + verb
    }
