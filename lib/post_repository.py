from lib.post import *

class PostRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        results = []
        rows = self._connection.execute("SELECT * FROM posts")
        for row in rows:
            item = Post(row["id"], row["post_title"], row["post_contents"], row["post_views"], row["user_account_id"])
            results.append(item)
        return results
    
    def find(self, post_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE id = %s", [post_id])
        row = rows[0]
        return Post(row["id"], row["post_title"], row["post_contents"], row["post_views"], row["user_account_id"])
    
    def create(self, post):
        self._connection.execute("INSERT INTO posts (post_title, post_contents, post_views, user_account_id) VALUES (%s, %s, %s, %s)", [post.title, post.contents, post.views, post.user_account_id])
        return None
    
    def delete(self, id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [id])
        return None