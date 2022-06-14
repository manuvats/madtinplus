import random
import string
from django.contrib.auth.hashers import make_password

#from customer.models import Account

#from django.contrib.auth.models import User

def set_random_password():
        ## length of password
        length = random.randint(6,10)
        
        #define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        #combine data
        all = lower + upper + num + symbols

        #use random
        temp = random.sample(all, length)

        #create the password
        password = "".join(temp)

        #hidden_password = make_password(password)

        #Klass = instance.__class__
        #qs_exists = Klass.objects.filter(password=new_password).exists()
        #if qs_exists:
        #    return set_random_password(instance)
        return password    


