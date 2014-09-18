import argparse

from instant_rst.config import DEFAULT_FILE, DEFAULT_PORT, DEFAULT_BROWSER, \
    TEMPLATE_DIR, STATIC_DIR

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
    parser.add_argument('-s', '--static-dir', dest='static_dir',
                        default=STATIC_DIR,
                        help='Directory with static files for rendering')
    parser.add_argument('-t', '--template-dir', dest='template_dir',
                        default=TEMPLATE_DIR,
                        help='Directory with template files for rendering')

    return parser.parse_args()
