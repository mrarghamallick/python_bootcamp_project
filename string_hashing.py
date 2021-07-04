import hashlib
str=input('Enter a string to hash: ')

obj=hashlib.md5(str.encode())
hashed_str=obj.hexdigest()

print("The hashed string using md5 algorithm is : "+ hashed_str)


obj2=hashlib.sha1(hashed_str.encode())
hashed_str2=obj2.hexdigest()

print("The hashed string (after 2 times) using md5 and sha1 algorithm is : "+ hashed_str2)


obj3=hashlib.blake2b(hashed_str2.encode())
hashed_str3=obj3.hexdigest()

print("The hashed string (after 3 times) using md5 and sha1 and blake2b algorithm is : "+ hashed_str3)