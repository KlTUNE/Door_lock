import hashlib

def check(password, hashed_password="ce62b07760701545d0a7efdd09b5482a272dbfbf0bd7e6c3794f1746bf03deb5"):
    hashed_pw = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if (hashed_pw == hashed_password):
        return True
    else:
        return False

def password2hash(password):
    hashed_pw = hashlib.sha256(password.encode("utf-8")).hexdigest()
    print(hashed_pw)
    return hashed_pw

if __name__ == '__main__':
    # password2hash("")
    print(check(""))