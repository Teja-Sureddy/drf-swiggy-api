from django.contrib import admin
from .models_list.role import Role
from .models import User
from .models_list.restaurant import Restaurant
from .models_list.menu import Menu
from .models_list.order import Order
from .models_list.ordered_items import OrderedItems

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderedItems)