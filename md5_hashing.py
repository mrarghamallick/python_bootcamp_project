import hashlib
str=input('Enter a string to hash: ')

obj=hashlib.md5(str.encode())
hashed_str=obj.hexdigest()

print("The hashed string using md5 algorithm is : "+ hashed_str)