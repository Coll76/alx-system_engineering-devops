import base64

base64_string = "vghpcyBpcyBteSBsb2dpbg=="
decoded_string = base64.b64decode(base64_string).decode()

print(decoded_string)
