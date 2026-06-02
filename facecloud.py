import datetime

class User:
    def __init__(self, user_id: int, email: str, password: str):
        self.id = user_id
        self.email = email
        self.password = password
        self.profile = None

    @staticmethod
    def register(user_id: int, email: str, password: str, existing_emails: list) -> 'User':
        """
        Реєстрація нового користувача.
        Нетривіальна логіка: валідація email, довжини пароля та унікальності.
        """
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Некоректний формат email")
        
        # ЛОГІЧНИЙ БАГ №1: Замість < 6 написано <= 6. 
        # Пароль рівно з 6 символів буде помилково заблоковано.
        if len(password) <= 6: 
            raise ValueError("Пароль занадто короткий (мінімум 6 символів)")
            
        if email in existing_emails:
            raise ValueError("Користувач з таким email вже існує")
            
        return User(user_id, email, password)

    def login(self, input_password: str) -> bool:
        """Авторизація користувача за паролем."""
        return self.password == input_password


class Profile:
    def __init__(self, nickname: str, bio: str = ""):
        self.nickname = nickname
        self.bio = bio

    def update_profile(self, new_nickname: str, new_bio: str) -> None:
        """
        Оновлення профілю.
        Нетривіальна логіка: перевірка довжини нікнейму та дозволених символів.
        """
        if len(new_nickname) < 3 or len(new_nickname) > 15:
            raise ValueError("Нікнейм повинен бути від 3 до 15 символів")
            
        if not new_nickname.isalnum():
            raise ValueError("Нікнейм може містити лише букви та цифри")
            
        self.nickname = new_nickname
        self.bio = new_bio


class Post:
    def __init__(self, post_id: int, content: str):
        self.id = post_id
        self.content = content
        self.created_at = datetime.datetime.now()

    @staticmethod
    def create_post(post_id: int, content: str) -> 'Post':
        """
        Створення публікації.
        Нетривіальна логіка: перевірка на порожнечу та ліміт символів (макс 280).
        """
        # ЛОГІЧНИЙ БАГ №2: Відсутній .strip(). 
        # Пост із одних пробілів "   " успішно створиться, хоча він порожній.
        if len(content) == 0:
            raise ValueError("Публікація не може бути порожньою")
            
        if len(content) > 280:
            raise ValueError("Максимальна довжина публікації — 280 символів")
            
        return Post(post_id, content)