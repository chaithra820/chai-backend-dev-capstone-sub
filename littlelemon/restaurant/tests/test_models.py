from django.test import TestCase
from reastaurant.models import Menu

class MenuModelTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(title="Pizza", price=10, inventory=5)
        self.assertEqual(str(item), "Pizza")
