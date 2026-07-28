from pathlib import Path
import platform
from datetime import datetime
import os


class File:

    # ---------- Read ----------

    @staticmethod
    def read(path, encoding="utf-8"):
        return Path(path).read_text(encoding=encoding)

    @staticmethod
    def read_bytes(path):
        return Path(path).read_bytes()

    # ---------- Write ----------

    @staticmethod
    def write(path, content, encoding="utf-8"):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path.write_text(content, encoding=encoding)

    @staticmethod
    def write_bytes(path, content):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        return path.write_bytes(content)

    # ---------- Append ----------

    @staticmethod
    def append(path, content, encoding="utf-8"):
        with Path(path).open("a", encoding=encoding) as f:
            f.write(content)

    # ---------- Info ----------

    @staticmethod
    def exists(path):
        return Path(path).exists()

    @staticmethod
    def is_file(path):
        return Path(path).is_file()

    @staticmethod
    def is_dir(path):
        return Path(path).is_dir()

    @staticmethod
    def name(path):
        return Path(path).name

    @staticmethod
    def stem(path):
        return Path(path).stem

    @staticmethod
    def suffix(path):
        return Path(path).suffix

    @staticmethod
    def parent(path):
        return str(Path(path).parent)

    @staticmethod
    def size(path):
        return Path(path).stat().st_size

    @staticmethod
    def created(path):
        return datetime.fromtimestamp(Path(path).stat().st_ctime)

    @staticmethod
    def modified(path):
        return datetime.fromtimestamp(Path(path).stat().st_mtime)

    @staticmethod
    def accessed(path):
        return datetime.fromtimestamp(Path(path).stat().st_atime)

    # ---------- System ----------

    @staticmethod
    def os_name():
        return platform.system()

    @staticmethod
    def os_release():
        return platform.release()

    @staticmethod
    def os_version():
        return platform.version()

    @staticmethod
    def architecture():
        return platform.machine()

    @staticmethod
    def python_version():
        return platform.python_version()

    @staticmethod
    def current_dir():
        return os.getcwd()

    @staticmethod
    def home():
        return str(Path.home())

    @staticmethod
    def now():
        return datetime.now()

    @staticmethod
    def timestamp():
        return datetime.now().timestamp()
