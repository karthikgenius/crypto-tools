from cryptography.fernet import Fernet

key = '' #Give your key here

f = Fernet(key)

token = '' #Give your Token here
my_str_as_bytes = str.encode(token)

print(f.decrypt(my_str_as_bytes))
