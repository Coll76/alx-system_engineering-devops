import base64

encoded_string = "VG8gZXJyIGlzIGh1bWFuLCBidXQgdG8gcmVhbGx5IGZvdWwgdGhpbmdzIHVwIHlvdSBuZWVkIGEgY29tcHV0ZXIuCiAgICAtLSBQYXVsIFIuIEVocmxpY2g="
decoded_string = base64.b64decode(encoded_string).decode()

print(decoded_string)

try:
        username, password = decoded_string.split(":")
        print(f"Username: {username}")
        print(f"Password: {password}")
except ValueError as e:
        print(f"Error: {e}")
