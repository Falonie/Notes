from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        # return generate_password_hash()

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


if __name__ == '__main__':
    u = User()
    u.password = 'tom'
    # print(u.password)
    print(u.password_hash)
    print(u.verify_password('tome'))
