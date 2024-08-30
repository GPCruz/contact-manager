# test_user_service.py
import unittest
from unittest.mock import MagicMock, patch

from sqlalchemy.exc import SQLAlchemyError

from db.models.user_model import User
from services.user_service import UserService


class TestUserService(unittest.TestCase):
    pass
    @patch('services.user_service.get_session')
    def test_create_user_success(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session

        user_service = UserService()
        new_user = user_service.create_user('testuser', 'Test User', 'password123')

        self.assertIsNotNone(new_user)
        mock_session.add.assert_called_once()

    @patch('services.user_service.get_session')
    def test_create_user_failure(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_session.add.side_effect = SQLAlchemyError

        user_service = UserService()
        new_user = user_service.create_user('testuser', 'Test User', 'password123')

        self.assertIsNone(new_user)

    # @patch('services.user_service.get_session')
    # def test_authenticate_user_success(self, mock_get_session):
    #     mock_session = MagicMock()
    #     mock_get_session.return_value.__enter__.return_value = mock_session
    #     mock_user = User(username='testuser', password_hash='hashedpassword')
    #     mock_session.query.return_value.filter_by.return_value.first.return_value = mock_user

    #     with patch('werkzeug.security.check_password_hash', return_value=True):
    #         user_service = UserService()
    #         user = user_service.authenticate_user('testuser', 'password123')

    #         self.assertIsNotNone(user)

    @patch('services.user_service.get_session')
    def test_authenticate_user_failure(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.filter_by.return_value.first.return_value = None

        user_service = UserService()
        user = user_service.authenticate_user('testuser', 'password123')

        self.assertIsNone(user)

    @patch('services.user_service.get_session')
    def test_get_user_success(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_user = User(id=1, username='testuser')
        mock_session.query.return_value.get.return_value = mock_user

        user_service = UserService()
        user = user_service.get_user(1)

        self.assertIsNotNone(user)

    @patch('services.user_service.get_session')
    def test_get_user_failure(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.get.return_value = None

        user_service = UserService()
        user = user_service.get_user(1)

        self.assertIsNone(user)

    @patch('services.user_service.get_session')
    def test_update_user_success(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_user = User(id=1, username='testuser')
        mock_session.query.return_value.get.return_value = mock_user

        user_service = UserService()
        updated_user = user_service.update_user(1, username='newusername', password='newpassword')

        self.assertIsNotNone(updated_user)
        self.assertEqual(updated_user.username, 'newusername')

    @patch('services.user_service.get_session')
    def test_update_user_failure(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.get.return_value = None

        user_service = UserService()
        updated_user = user_service.update_user(1, username='newusername', password='newpassword')

        self.assertIsNone(updated_user)

    @patch('services.user_service.get_session')
    def test_delete_user_success(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_user = User(id=1, username='testuser')
        mock_session.query.return_value.get.return_value = mock_user

        user_service = UserService()
        result = user_service.delete_user(1)

        self.assertTrue(result)
        mock_session.delete.assert_called_once_with(mock_user)

    @patch('services.user_service.get_session')
    def test_delete_user_failure(self, mock_get_session):
        mock_session = MagicMock()
        mock_get_session.return_value.__enter__.return_value = mock_session
        mock_session.query.return_value.get.return_value = None

        user_service = UserService()
        result = user_service.delete_user(1)

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()