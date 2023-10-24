from django.test import TestCase
from datetime import date

from modules.CompanyInfo import CompanyInfo

# Create your tests here.
company = CompanyInfo()

print(company.__dict__)