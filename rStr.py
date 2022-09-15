import random
import string

# printing lowercase
def randomString(stringLength=10):
    letters = string.ascii_lowercase
    x = ''.join(random.choice(letters) for i in range(stringLength))
    return x

