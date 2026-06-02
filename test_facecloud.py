import pytest
from facecloud import User, Profile, Post

# --- ТЕСТИ КЛАСУ USER ---

def test_register_success():
    # Arrange [cite: 644, 647, 873]
    uid, email, password = 1, "test@me.com", "pass1234"
    existing = []
    # Act [cite: 644, 647, 873]
    user = User.register(uid, email, password, existing)
    # Assert [cite: 644, 647, 873]
    assert user.id == uid
    assert user.email == email

def test_register_invalid_email():
    # Arrange & Act & Assert pytest --cov=facecloud --cov-report=term
    with pytest.raises(ValueError, match="Некоректний формат email"):
        User.register(2, "bad_email", "pass1234", [])

def test_register_too_short_password():
    # Arrange & Act & Assert (BVA: довжина 5) 
    with pytest.raises(ValueError, match="Пароль занадто короткий"):
        User.register(3, "valid@me.com", "12345", [])

def test_register_duplicate_email():
    # Arrange & Act & Assert 
    with pytest.raises(ValueError, match="Користувач з таким email вже існує"):
        User.register(4, "test@me.com", "pass1234", ["test@me.com"])

def test_login_success():
    # Arrange 
    user = User(1, "test@me.com", "secure123")
    # Act & Assert 
    assert user.login("secure123") is True

def test_login_wrong_password():
    # Arrange 
    user = User(1, "test@me.com", "secure123")
    # Act & Assert 
    assert user.login("wrong_password") is False


# --- ТЕСТИ КЛАСУ PROFILE ---

def test_update_profile_success():
    # Arrange 
    profile = Profile("oldname", "old bio")
    # Act 
    profile.update_profile("alex99", "New bio text")
    # Assert 
    assert profile.nickname == "alex99"
    assert profile.bio == "New bio text"

def test_update_profile_too_short_nickname():
    # Arrange 
    profile = Profile("oldname")
    # Act & Assert (BVA: довжина 2) 
    with pytest.raises(ValueError, match="Нікнейм повинен бути від 3 до 15 символів"):
        profile.update_profile("jo", "bio")

def test_update_profile_invalid_symbols():
    # Arrange 
    profile = Profile("oldname")
    # Act & Assert 
    with pytest.raises(ValueError, match="Нікнейм може містити лише букви та цифри"):
        profile.update_profile("usr_1!", "bio")


# --- ТЕСТИ КЛАСУ POST ---

def test_create_post_success():
    # Arrange & Act 
    post = Post.create_post(100, "Valid post text")
    # Assert 
    assert post.id == 100
    assert post.content == "Valid post text"

def test_create_post_empty():
    # Arrange & Act & Assert (BVA: довжина 0) 
    with pytest.raises(ValueError, match="Публікація не може бути порожньою"):
        Post.create_post(101, "")

def test_create_post_too_long():
    # Arrange & Act & Assert (BVA: довжина 281) 
    with pytest.raises(ValueError, match="Максимальна довжина публікації"):
        Post.create_post(102, "a" * 281)