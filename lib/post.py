class Post:
    def __init__(self, id, title, contents, views, user_account_id):
        self.id = id
        self.title = title
        self.contents = contents
        self.views = views
        self.user_account_id = user_account_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.contents}, {self.views}, {self.user_account_id})"
