
from api.services.user_service import UserService


class AuthService:
    @staticmethod
    def login(username: str, password: str) -> str:
        user = UserService.authenticate_user(username, password)
        if user:
            return user.generate_auth_token()
        return None
    
    @staticmethod
    def generate_auth_token(user_id: int) -> str:
        user = UserService.get_user(user_id)
        if user:
            return user.generate_auth_token()
        return None