from django.db import models
import string
import random

def gen_unique_code():
    length = 8
    while True:
        generated_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k= length))
        if Gang.objects.filter(code = generated_code).count() == 0:
            break

# Create your models here.
class Gang(models.Model):
    code = models.CharField(max_length= 8, default= "", unique= True)
    host = models.CharField(max_length= 50, unique= True)
    can_guests_pause = models.BooleanField(default= False, null= False)
    votes_to_skip = models.IntegerField(default= 1, null= False)
    created_at = models.DateTimeField(auto_now_add= True)

    
