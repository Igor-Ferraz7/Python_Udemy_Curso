class Connection:
    def __init__(self):
        self.user = None
        self.password = None

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

u1 = Connection.create_with_auth('Igor', '3107')
print(u1.user, u1.password)