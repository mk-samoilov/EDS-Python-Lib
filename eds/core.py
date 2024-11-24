import json, hashlib
from eds.exceptions import DecryptFileError


class EDSFile:
    def __init__(self, filename: str, key: str):
        self.filename = filename
        self.key = self._format_key(key=key)

    @staticmethod
    def _format_key(key: str):
        if isinstance(key, str):
            key = key.encode()
        return hashlib.sha256(key).digest()

    def _generate_key_stream(self, length):
        key_stream = bytearray()
        while len(key_stream) < length:
            key_stream.extend(hashlib.sha256(self.key + len(key_stream).to_bytes(4, "big")).digest())
        return bytes(key_stream[:length])

    def _xor_encrypt_decrypt(self, data):
        key_stream = self._generate_key_stream(len(data))
        return bytes(a ^ b for a, b in zip(data, key_stream))

    def read(self):
        try:
            with open(self.filename, "rb") as file:
                encrypted_data = file.read()

            decrypted_data = self._xor_encrypt_decrypt(encrypted_data)
            return json.loads(decrypted_data)

        except UnicodeDecodeError:
            raise DecryptFileError

    def write(self, data: str or dict or list):
        json_data = json.dumps(data, indent=2).encode()
        encrypted_data = self._xor_encrypt_decrypt(json_data)

        with open(self.filename, "wb") as file:
            file.write(encrypted_data)
