import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16
# é
password = "".join(random.sample(total, length))

print(password)