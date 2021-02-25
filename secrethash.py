import glob
import hashlib

class hasher:

    def __init__(self):
        self.hash_md5 = hashlib.md5()
        self.hexdigest = ''

    def _update(self, fname):
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(2 ** 20), b""):
                self.hash_md5.update(chunk)
        self.hexdigest = self.hash_md5.hexdigest()

    def generate(self, path):
        filenames = glob.glob(path)
        filenames = sorted(filenames)
        for filename in filenames:
            self._update(filename)

    def generate_text(self, text):
        self.hash_md5.update(text.encode('utf-8'))
        self.hexdigest = self.hash_md5.hexdigest()
