from lib.post_repository import *
from lib.post import *
from lib.user_repository import *
from lib.user import *

def test_all(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post(1, 'Paul is a traitor', 'He left the band', 20, 1),
        Post(2, 'John is full of it', 'I left because of him', 50, 2)
    ]
    

def test_find(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    result = repository.find(2)
    assert result == Post(2, 'John is full of it', 'I left because of him', 50, 2)

def test_create(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    user_repository = UserRepository(db_connection)
    user = User(None, "George", "george@beatles.net")
    user_repository.create(user)
    post_repository = PostRepository(db_connection)
    post = Post(None, "Hey guys I wrote a song", "No really, I did", 100, 3)
    post_repository.create(post)
    result = post_repository.all()
    assert result == [
        Post(1, 'Paul is a traitor', 'He left the band', 20, 1),
        Post(2, 'John is full of it', 'I left because of him', 50, 2),
        Post(3, "Hey guys I wrote a song", "No really, I did", 100, 3)
    ]

def test_delete(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [Post(2, 'John is full of it', 'I left because of him', 50, 2)]