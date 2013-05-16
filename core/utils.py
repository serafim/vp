# coding=utf-8
from hashlib import md5
from random import getrandbits
from datetime import datetime


def generate_user_id():
    user_id = md5()
    user_id.update(str(datetime.now()) + str(getrandbits(128)))
    return user_id.hexdigest()