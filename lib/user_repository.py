from lib.user import *

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        results = []
        rows = self._connection.execute("SELECT * FROM user_accounts")
        for row in rows:
            item = User(row["id"], row["username"], row["email_address"])
            results.append(item)
        return results
    
    def find(self, user_id):
        rows = self._connection.execute("SELECT * FROM user_accounts WHERE id = %s", [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email_address"])
    
    def create(self, user):
        self._connection.execute("INSERT INTO user_accounts (username, email_address) VALUES (%s, %s)", [user.username, user.email])
        return None
    
    def delete(self, id):
        self._connection.execute("DELETE FROM user_accounts WHERE id = %s", [id])
        return None