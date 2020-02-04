from django.test import TestCase
from .models import Picture,Location,Category

# Create your tests here.
class LocationTest(TestCase):
    def setUp(self):
        self.location = Location(location = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(category= 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))
    
    
    def test_save(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

class PictureTest(TestCase):
    def setUp(self):
        self.location = Location(location= 'Nairobi')
        self.location.save()
        self.category = Category(category = 'Travel')
        self.category.save()
        self.image = Picture(image= 'images.jpeg', title= 'Nairobi', location = self.location, category = self.category)
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Picture))
    
    def test_save(self):
        self.image.save_images()
        image = Picture.objects.all()
        self.assertTrue(len(image) > 0)
        
    def save_images(self):
        self.save()
