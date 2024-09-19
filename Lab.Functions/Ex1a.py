from cryptography.fernet import Fernet

key = Fernet.generate_key()

cipher = Fernet(key)

user_input = input("Enter a string to encrypt: ")

encoded_string = user_input.encode()

encrypted_string = cipher.encrypt(encoded_string)
print(f"Encrypted: {encrypted_string}")


decrypted_string = cipher.decrypt(encrypted_string)

decoded_string = decrypted_string.decode()
print(f"Decrypted: {decoded_string}")
