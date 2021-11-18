import os, hashlib
from django.core.exceptions import ValidationError

def password_hashing(password, salt=None):
    """
    Password hashing method, Return hash_password and salt
    :param password: password to be hashed,
    :param salt: Default is none, If salt is not passed new salt will be generated
    :return: password_hash, salt
    """
    if not salt:
        # create salt based on urandom
        salt = os.urandom(8).hex()
    hash = hashlib.sha512()
    # TODO: shouldn't this update function use password, salt??
    hash.update(('%s%s' % (password, salt)).encode('utf-8'))
    password_hash = hash.hexdigest()
    return (password_hash, salt)

def validate_request(keys, request_data):
    resp = {}
    for key in keys:
        if key not in request_data:
            raise ValidationError("Missing Key '{}' in request data".format(key))
        resp[key] = request_data[key]
    return resp 

def fetch_params(params):
    id = None
    order_by_created = False
    page_no = 1
    item_per_page = 10

    if "id" in params:
        try:
            id = int(params["id"])
        except:
            id = None

    if "order_by_created" in params:
        order_by_created = True

    if "page_no" in params:
        try:
            page_no = int(params["page_no"])
        except:
            page_no = 1

    if "item_per_page" in params:
        try:
            page_no = int(params["page_no"])
        except:
            page_no = 1
    return id, order_by_created, page_no, item_per_page
