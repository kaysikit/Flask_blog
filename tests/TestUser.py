import unittest
from flask_blog.models.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_create_user(self):
        self.assertIsNone(
            self.user.new(
                'DungeonMaster',
                '52625256ergr',
            ), None
        )

        self.assertTrue(
            self.user.new(
                'Test',
                'testing',
            ), True
        )

    def test_auth_user(self):
        self.assertTrue(
            self.user.autenfication(
                'DungeonMaster',
                '1628482000',
            ), True
        )

        self.assertIsNone(
            self.user.autenfication(
                'DFgfdgwrgr',
                'gfdgrgwgrg',
            ), None
        )

    def test_replace_password(self):
        self.assertTrue(
            self.user.update_password(
                'DangerMaster',
                '52625256ergrgf',
            ), True
        )

    if __name__ == "__main__":
        unittest.main()
