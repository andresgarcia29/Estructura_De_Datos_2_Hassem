import os
from endpoint import APP

if __name__ == '__main__':
    PORT = 5000
    APP.run('0.0.0.0', port=PORT, threaded=True, debug=True)
