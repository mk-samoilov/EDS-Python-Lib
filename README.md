# EDS (Encrypted Data Storage)

My Python library for working with encrypted files by key.

## Overview

EDS provides a simple way to store sensitive data in encrypted files while maintaining easy access through a key-based system. It's perfect for storing configuration files, credentials, and other sensitive JSON data that needs basic encryption.

## Features

- 🔒 XOR encryption with SHA-256 key hashing
- 📄 JSON data format support
- 🔑 Simple key-based file access

## Quick Start

Here's a simple example of how to use EDS:

```python
from eds.core import EDSFile

# Initialize encrypted file
eds_file = EDSFile(filename="login_data.eds", key="qwe123")

# Write data
data = {
    "api_key": "777-QWE-777",
    "credentials": {
        "username": "admin",
        "password": "admin"
    }
}
eds_file.write(data)

# Read data
stored_data = eds_file.read()
print(stored_data)
```

## Documentation

### EDSFile Class

The main class for handling encrypted file operations.

#### Constructor

```python
EDSFile(filename: str, key: str)
```

- `filename`: Path to the encrypted file
- `key`: Encryption/decryption key


#### Methods

##### write(data: Union[str, dict, list]) -> None

Encrypts and writes data to file

- `data`: JSON-serializable data (string, dictionary, or list)


##### read() -> Union[str, dict, list]

Reads and decrypts file content

- Returns: Decrypted JSON data
- Raises: `DecryptFileError` if decryption fails


## Security Considerations

- EDS uses basic XOR encryption with SHA-256 key hashing
- Suitable for basic data protection needs
- Not recommended for highly sensitive data requiring military-grade encryption
- Key management is the user's responsibility


## Error Handling

The library includes the `DecryptFileError` exception which is raised when:

- The wrong decryption key is used
- The file content is corrupted
- The content cannot be decoded as JSON

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Disclaimer

This library provides basic encryption and should not be used as the sole protection for highly sensitive data. For production systems requiring high security, please use established encryption libraries and consult with security experts.