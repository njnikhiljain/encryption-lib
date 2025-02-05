# Encryption Library

A simple encryption library for projects.

## Installation

```bash
pip install git+https://github.com/njnikhiljain/encryption-lib.git

## Update the setting.py with below values
SALT_KEY = "your salt key"
EXPIRATION_TIME = 3600  # 1 hour

## Usage of the library

from encryption_lib.encryption import generate_auth_token, verify_auth_token

token = generate_auth_token("username", "org_id", "org_name")
is_valid = verify_auth_token(token, "username", "org_id", "org_name")

