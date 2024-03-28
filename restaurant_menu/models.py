from django.db import models
from django.contrib.auth.models import User

# The first word will be used by the code in the django project
# The second will be used by the front end on the website
# This will  act as a list of values that the cooks can choose from like a drop down list

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts")
)

# If the status is 0, the selection will be crossed out.
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    # So the author field will be associated with the User table provided by django up at the top of the file.  
    # If the author is “john” , and he is deleted, then all the meals that he has will be deleted as well. 
    # The CASCADE word means delete everything for that user.
    # Alternatively, you can put PROTECT which prohibits the deletion of a user, thereby protecting the meals associcated with that user as well.
    # Leaving it on CASCADE is better for Data Intergrity though, so I will keep it here.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    # In the next two lines below, whenever the cook creates a new item or updates the item, the timestamp will be recorded. 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal