import unittest
from unittest.mock import patch, MagicMock
from services.user_service import UserService
from db.models.user_model import User
from db.db_driver import session

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.user_service = UserService()
        self.new_user = {
            "username": "testuser",
            "password": "testpassword"
        }

    @patch('services.user_service.session')
    def test_create_user(self, mock_session):
        mock_session.add = MagicMock()
        mock_session.commit = MagicMock()

        user = self.user_service.create_user(self.new_user["username"], self.new_user["password"])

        self.assertEqual(user.username, self.new_user["username"])
        self.assertNotEqual(user.password_hash, self.new_user["password"])  # Password should be hashed
        mock_session.add.assert_called_once_with(user)
        mock_session.commit.assert_called_once()

    # @patch('services.user_service.session')
    # def test_authenticate_user(self, mock_session):
    #     mock_user = User(username=self.new_user["username"], password_hash="hashedpassword")
    #     mock_session.query().filter_by().first.return_value = mock_user

    #     with patch('werkzeug.security.check_password_hash', return_value=True):
    #         user = self.user_service.authenticate_user(self.new_user["username"], self.new_user["password"])

    #     self.assertIsNotNone(user)
    #     self.assertEqual(user.username, self.new_user["username"])

    # @patch('services.user_service.session')
    # def test_authenticate_user_invalid_password(self, mock_session):
    #     mock_user = User(username=self.new_user["username"], password_hash="hashedpassword")
    #     mock_session.query().filter_by().first.return_value = mock_user

    #     with patch('werkzeug.security.check_password_hash', return_value=False):
    #         user = self.user_service.authenticate_user(self.new_user["username"], "wrongpassword")

    #     self.assertIsNone(user)

    # @patch('services.user_service.session')
    # def test_authenticate_nonexistent_user(self, mock_session):
    #     mock_session.query().filter_by().first.return_value = None

    #     user = self.user_service.authenticate_user("nonexistent", "password")

    #     self.assertIsNone(user)

if __name__ == '__main__':
    unittest.main()