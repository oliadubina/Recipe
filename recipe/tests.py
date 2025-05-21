from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name='Dessert')
        self.assertEqual(category.name, 'Dessert')
        self.assertEqual(str(category), 'Dessert')
class RecipeModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Dessert')

    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            title='Chocolate Cake',
            description='Delicious chocolate cake',
            instructions='Mix, bake, enjoy.',
            ingredients='Chocolate, flour, sugar, eggs',
            category=self.category
        )
        self.assertEqual(recipe.title, 'Chocolate Cake')
        self.assertEqual(recipe.category.name, 'Dessert')
        self.assertIn('chocolate', recipe.description.lower())
        self.assertEqual(str(recipe), 'Chocolate Cake')
