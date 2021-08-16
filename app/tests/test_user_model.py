from django.test import TestCase
from app.models import User

class TestUserModel(TestCase):
    def setUp(self):
        User.objects.create(
            email = 'prissy@gmail.com',
            username = 'Prissy',
            password = 'Prissy@7'
        )

    def test_user_created(self):
        user = User.objects.get(username='Prissy')