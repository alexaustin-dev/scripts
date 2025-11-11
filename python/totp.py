# Simple script to generate secrets for TOTP to use with IT Glue and Duo Hardware Token

import base64
import secrets

# Generate 20 random bytes (160 bits)
secret_bytes = secrets.token_bytes(20)

# Convert to hexadecimal (40 characters)
hex_secret = secret_bytes.hex()

# Convert to base32 (for IT Glue)
base32_secret = base64.b32encode(secret_bytes).decode("utf-8").rstrip("=")

print("\n")
print(f"Enter this into IT Glue OTP: {base32_secret}\n")
print(f"Copy paste this into Duo Hardware Token: ITGLUE,{hex_secret},30\n")
print("The serial number needs to be unique per token.")
print("E.g. ITGLUE-1234567890,hexadecimalkey,timestep\n")
