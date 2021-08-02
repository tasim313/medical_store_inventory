from django.contrib import admin

'''''
from django.contrib.auth.admin import UserAdmin

from App_Login.models import CustomUser, PharmacyAdmin, PharmacyManager, Employee


class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(PharmacyAdmin)
admin.site.register(PharmacyManager)
admin.site.register(Employee)

'''''

from django.contrib.auth.admin import UserAdmin

from App_Login.models import CustomUser, Admin, Manager, Employee

admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Manager)
admin.site.register(Employee)