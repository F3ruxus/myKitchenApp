from typing import Any
from django.views import generic
# With this we are asking for the data from the database table
from .models import Item

# This code is to transer data to the HTML frontend from the python and django backend
# We are using a class based system but you could also use a function based systme as well.

# Now we don't have any data, any rows in that table.
# But when we add data later on in the admin interface
# as a cook, we will add some meals, and so on.
# Then this queryset will get those data.
# You can order them using the order_by method.
# You can order them by one of these fields.
# For example, let's take date_created.
# I'll copy that and put it here as a string
# inside quotes, date_created.
# And if you want to reverse the order,
# you just enter a minus before this, so -date_created.

# We are going to have to create the index.html and the menu_item_detail.html files 


class MenuList(generic.ListView):
    queryset = Item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        # So the context is a dictionary.
        # And then from your HTML templates,
        # you can access the keys of that dictionary as variables.
        context = {"meals": ["Pizza", "Pasta"],
                   "ingredients": ["things"]}
        return context


class MenuItemDetail(generic.DetailView):
    model = Item
    template_name = "menu_item_detail.html"