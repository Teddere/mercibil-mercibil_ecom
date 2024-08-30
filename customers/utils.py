import random
import string


# generate slug article
def generate_password():
    letters = string.ascii_letters + string.digits
    pwd = ''.join(random.choice(letters) for _ in range(10))
    return pwd