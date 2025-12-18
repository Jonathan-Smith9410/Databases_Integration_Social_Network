from lib.user import *

"""
Constructs with a username and email
"""

def test_constructs():
    user = User(1, "Test Username", "Test Email")
    assert user.id == 1
    assert user.username == "Test Username"
    assert user.email == "Test Email"

def test_equality():
    user1 = User(1, "Test Username", "Test Email")
    user2 = User(1, "Test Username", "Test Email")
    assert user1 == user2