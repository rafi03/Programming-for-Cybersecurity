import pytest
from password_checker import is_strong_password

def test_short_password():
    """Test that short passwords fail the check"""
    assert is_strong_password("Abc1!") == False

def test_missing_uppercase():
    """Test that passwords without uppercase fail the check"""
    assert is_strong_password("abcdef1!") == False

def test_missing_digit():
    """Test that passwords without digits fail the check"""
    assert is_strong_password("Abcdefg!") == False

def test_missing_special():
    """Test that passwords without special characters fail the check"""
    assert is_strong_password("Abcdef12") == False

def test_strong_password():
    """Test that strong passwords pass the check"""
    assert is_strong_password("Abcdef1!") == True