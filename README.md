# Encryption Library

A simple encryption library for projects.

## Installation

```bash
pip install git+https://github.com/njnikhiljain/encryption-lib.git

## Usage of the library

from encryption_lib.utils import encrypt_data, verify_data

token = encrypt_data("username", "org_id", "org_name")
is_valid = verify_data(token, "username", "org_id", "org_name")

