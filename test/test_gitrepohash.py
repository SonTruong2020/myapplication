import unittest
from app import gitrepohash

def test_appexecution() :
    result = gitrepohash.get_git_repo_hash()
    assert result
