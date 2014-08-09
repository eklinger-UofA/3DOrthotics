from django.contrib import admin
# import models once i am done writing them
# from <app>.models import <model_name>, <model_name>
from clients.models import Client, Perscription, Insurance, Claim

# Register your models here.
# admin.site.register(<model_name>)
admin.site.register(Client)
admin.site.register(Perscription)
admin.site.register(Insurance)
admin.site.register(Claim)
