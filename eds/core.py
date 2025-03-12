import hashlib
import pickle

from .exceptions import DecryptFileError, EncryptFileError

class XORCrypter:
    def __init__(self, key: str):
        self.key = self.format_key(key)

    @staticmethod
    def format_key(key: str) -> bytes:
        return hashlib.sha256(key.encode()).digest()

    def crypt(self, data: bytes) -> bytes:
        return bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(data)])

class EDSFile:
    def __init__(self, filename: str, key: str):
        self.filename = str(filename)
        self.crypter = XORCrypter(key=str(key))

    def read(self):
        try:
            with open(self.filename, "rb") as file:
                encrypted_data = file.read()
                if not encrypted_data:
                    raise DecryptFileError("File is empty")
                decrypted_data = self.crypter.crypt(encrypted_data)
                return pickle.loads(decrypted_data)
        except (pickle.UnpicklingError, UnicodeDecodeError, EOFError) as e:
            raise DecryptFileError from e

    def write(self, new_data: object):
        if new_data is None:
            raise EncryptFileError("'None' is not writeable.")

        try:
            serialized_data = pickle.dumps(new_data)
            encrypted_data = self.crypter.crypt(serialized_data)
            with open(self.filename, "wb") as file:
                file.write(encrypted_data)
        except (TypeError, pickle.PicklingError) as e:
            raise EncryptFileError from e
