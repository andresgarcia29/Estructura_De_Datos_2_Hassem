"""
  Fields necessaries to complete the request
"""

contracts = {
    "teacher": ['name', 'email', 'cellphone'],
    "user": ['name', 'password', 'rol', 'status'],
    "rol": ['name', 'status'],
    "period": ['name', 'start', 'finish', 'status'],
    "group": ['name', 'status'],
    "offer": ['teacher', 'list', 'group', 'period', 'status']
}
