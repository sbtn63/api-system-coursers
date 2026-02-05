from django.test import TestCase
from django.contrib.auth.models import User
from institutions.models import Institution

class InstitutionTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )
        
        self.institution = Institution.objects.create(
            name="INSTITUTION TEST",
            emblem="https://emblem.tst.com",
            description="TEST DESCRIPTION",
            user=self.user
        )
    
    def test_institution_creation(self):
        self.assertEqual(str(self.institution), "INSTITUTION TEST")