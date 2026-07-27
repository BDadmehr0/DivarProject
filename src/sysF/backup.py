from pathlib import Path
import shutil
import hashlib


class FileManager:

    def __init__(self, data="data", backup="backup"):
        self.data = Path(data)
        self.backup = Path(backup)

        self.data.mkdir(parents=True, exist_ok=True)
        self.backup.mkdir(parents=True, exist_ok=True)

    def sha256(self, file):
        h = hashlib.sha256()

        with open(file, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                h.update(chunk)

        return h.hexdigest()

    # ----------------------------
    # اولین بکاپ
    # ----------------------------

    def backup_all(self):

        for file in self.data.rglob("*"):

            if not file.is_file():
                continue

            dst = self.backup / file.relative_to(self.data)

            dst.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(file, dst)

    # ----------------------------
    # فقط فایل‌های تغییر کرده
    # ----------------------------

    def sync_backup(self):

        for file in self.data.rglob("*"):

            if not file.is_file():
                continue

            dst = self.backup / file.relative_to(self.data)

            if not dst.exists():

                dst.parent.mkdir(parents=True, exist_ok=True)

                shutil.copy2(file, dst)

                continue

            if self.sha256(file) != self.sha256(dst):

                shutil.copy2(file, dst)

    # ----------------------------
    # بازیابی همه فایل‌ها
    # ----------------------------

    def restore_all(self):

        for file in self.backup.rglob("*"):

            if not file.is_file():
                continue

            dst = self.data / file.relative_to(self.backup)

            dst.parent.mkdir(parents=True, exist_ok=True)

            shutil.copy2(file, dst)