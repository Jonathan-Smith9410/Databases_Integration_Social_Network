from lib.post import *


"""
Constructs with an id, title, contents, views, user_account_id
"""

def test_construct():
    post = Post(1, "Test Title", "Test Contents", 20, 2)
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.contents == "Test Contents"
    assert post.views == 20
    assert post.user_account_id == 2

def test_equality():
    post1 = Post(1, "Test Title", "Test Contents", 20, 2)
    post2 = Post(1, "Test Title", "Test Contents", 20, 2)
    assert post1 == post2