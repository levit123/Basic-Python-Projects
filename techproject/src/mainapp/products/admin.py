from django.contrib import admin

# imports the models we've made for this project
from .models import Product

# registers the models we've made for this project
admin.site.register(Product)
