""" Test models for 'products' app"""
from django.test import TestCase
from .models import Category, Product


class TestCategoryModel(TestCase):
    """
    test the category model
    """

    def test_category_string_method_returns_name(self):
        """
        test category model string method
        """
        category = Category.objects.create(name="category_name")
        self.assertEqual(str(category), "category_name")

    def test_category_friendly_name_str_method(self):
        """
        testing category models friendly name string
        method returns friendly name
        """
        test_case = Category()
        test_case.friendly_name = "Friendly"
        self.assertEqual(test_case.get_friendly_name(), "Friendly")


class TestProductModel(TestCase):
    """
    test product model
    """
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_product_string_method_returns_name(self):
        """
        test product model string method
        """
        product = Product.objects.create(name="product_name", price=21.99)
        self.assertEqual(str(product), "product_name")

    def test_product_name_returns_name(self):
        """
        Test that the product name is returned
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, "The Winemaker's Wife")
        self.assertNotEqual(product.name, 'Ghosts')
        self.assertEqual(str(product), product.name)

    def test_product_description_returns_description(self):
        """
        Test that the product description is returned
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(
            product.description, "The author of the engrossing international bestseller The Room on Rue Amelie returns with a moving story set amid the champagne vineyards of northern France during the darkest days of World War II, perfect for fans of Kristin Hannah's The Nightingale. Champagne, 1940: Ines has just married Michel, the owner of storied champagne house Maison Chauveau, when the Germans invade. As the danger mounts, Michel turns his back on his marriage to begin hiding munitions for the Resistance. Ines fears they'll be exposed, but for Celine, half-Jewish wife of Chauveau's chef de cave, the risk is even greater rumours abound of Jews being shipped east to an unspeakable fate. When Celine recklessly follows her heart in one desperate bid for happiness, and Ines makes a dangerous mistake with a Nazi collaborator, they risk the lives of those they love and the champagne house that ties them together. New York, 2019: Liv Kent has just lost everything when her eccentric French grandmother shows up unannounced, insisting on a trip to France. But the older woman has an ulterior motive and a tragic, decades-old story to share. When past and present finally collide, Liv finds herself on a road to salvation that leads right to the caves of the Maison Chauveau."
        )
        self.assertNotEqual(product.description, 'Not made of wool')
