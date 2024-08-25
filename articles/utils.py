import random
import string


# generate slug article
def generate_slug():
    letters = string.ascii_letters + string.digits
    slug = ''.join(random.choice(letters) for _ in range(8))
    return slug