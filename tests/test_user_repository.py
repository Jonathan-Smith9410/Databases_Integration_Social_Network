from lib.user_repository import *
from lib.user import *

def test_all(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, 'John Lennon', 'john@beatles.net'),
        User(2, 'Paul McCartney', 'paul@beatles.net')
    ]
    

def test_find(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    result = repository.find(2)
    assert result == User(2, 'Paul McCartney', 'paul@beatles.net')

def test_create(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User(None, "George", "george@beatles.net")
    repository.create(user)
    result = repository.all()
    assert result == [
        User(1, 'John Lennon', 'john@beatles.net'),
        User(2, 'Paul McCartney', 'paul@beatles.net'),
        User(3, "George", "george@beatles.net")
    ]

def test_delete(db_connection):
    connection = db_connection
    connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [User(2, 'Paul McCartney', 'paul@beatles.net')]