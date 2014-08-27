import argparse

from instant_rst.config import DEFAULT_FILE, DEFAULT_PORT, DEFAULT_BROWSER

def parse():
    parser = argparse.ArgumentParser(description='Preview rst Instantly')
    parser.add_argument('-f', '--file', dest='filename',
                default=DEFAULT_FILE,
                help='The local filename for Converting')
    parser.add_argument('-b', '--browser', dest='browser',
                default='firefox',
                help='The browser command for viewing')
    parser.add_argument('-p', '--port', dest='port',
                default='5676',
                help='The port for server to use')
    return parser.parse_args()
