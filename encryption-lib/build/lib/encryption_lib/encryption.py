import hmac
import hashlib
import base64
import json
import time
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

# Define a secret salt key (keep it in environment variables)

def generate_auth_token(username: str, org_id: str, org_name: str) -> tuple:
    username_hashed = hashlib.sha256(username.encode('utf-8')).hexdigest()
    
    # Generate salt
    salt = org_id + settings.SALT_KEY + org_name.replace(" ", "")
    salted_username = username_hashed + salt  # Combine username hash and salt
    
    # Generate hashed password
    final_token = make_password(salted_username)
    
    # Add expiration time
    expire_time = int(time.time()) + settings.EXPIRATION_TIME
    
    # Create token payload
    token_payload = {
        "token": final_token,
        "expires": expire_time
    }
    
    # Encode payload to JSON string
    token_str = json.dumps(token_payload)
    
    # Base64 encode the final token
    encoded_token = base64.urlsafe_b64encode(token_str.encode()).decode()
    
    return encoded_token

def verify_auth_token(username: str, org_id: str, org_name: str, token: str) -> bool:
    try:
        # Decode Base64 token
        decoded_token = base64.urlsafe_b64decode(token).decode()
        token_data = json.loads(decoded_token)
        
        # Extract token and expiration time
        final_token = token_data["token"]
        expire_time = token_data["expires"]
        
        # Check expiration time
        if time.time() > expire_time:
            return False  # Token expired
        
        username_hashed = hashlib.sha256(username.encode('utf-8')).hexdigest()
        salt = org_id + settings.SALT_KEY + org_name.replace(" ", "")
        salted_username = username_hashed + salt  # Combine username hash and salt
        
        return check_password(salted_username, final_token)
    except Exception:
        return False  # Return false if decoding or validation fails
