import os
import secrets
import stat
import ubelt as ub

ADDITIONAL_DIRS = []

mod_dpath = os.path.dirname(os.path.abspath(__file__))

STATIC_DIR = os.path.join(mod_dpath, 'templates')
DEFAULT_FILE = os.path.join(mod_dpath, 'templates', "index.rst")
HOST = "127.0.0.1"
# PORT = 5000
PORT = 58772  # Picking a random non-dev port
URL =  f"http://127.0.0.1:{PORT}"
# BROWSER = 'firefox'
BROWSER = ''
# SECRET = 'JO34h#F*$HFHA@#&('

FLASK_STATIC_FOLDER = os.path.join(mod_dpath, 'static')
FLASK_TEMPLATE_FOLDER = os.path.join(mod_dpath, 'templates')


APP_NAME = "instant-rst"


def _secret_file():
    config_dpath = ub.Path.appdir(APP_NAME).ensuredir()
    return config_dpath / "secret_key"


def get_secret(env_var="SECRET_KEY", allow_generate=True, dev_mode=False) -> str:
    # 1) Environment takes precedence
    val = os.getenv(env_var)
    if val:
        return val

    # 2) Persistent file-based secret
    fpath = _secret_file()
    if fpath.exists():
        return fpath.read_text().strip()

    # 3) Generate new one and save securely
    if allow_generate:
        secret = secrets.token_urlsafe(32)
        fpath.write_text(secret)

        # Lock down permissions on POSIX
        try:
            os.chmod(fpath, stat.S_IRUSR | stat.S_IWUSR)
        except Exception:
            pass
        return secret

    # 4) Dev fallback: ephemeral
    if dev_mode:
        return secrets.token_urlsafe(32)

    raise RuntimeError(f"{env_var} is required in production")


_p1 = None
_p2 = None
