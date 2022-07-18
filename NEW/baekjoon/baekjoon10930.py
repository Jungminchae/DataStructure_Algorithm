import sys
from hashlib import sha256


input = sys.stdin.readline
string = input()
encoded_string = string.encode()
sha_string = sha256(encoded_string).hexdigest()
print(sha_string)