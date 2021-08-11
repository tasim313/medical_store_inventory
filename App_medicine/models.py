from django.db import models
from App_Login.models import Admin, Manager, Employee, CustomUser
# Create your models here.

'''''
class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='Admin')
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='Manager')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='Employee')
'''

'''''
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    user_info = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Company Name')
    lic_no = models.CharField(max_length=300, verbose_name='License Number')
    address = models.CharField(max_length=300, verbose_name='Company Headquarter Address')
    cont_num = models.CharField(max_length=264, verbose_name='Company Contact Information')
    email = models.EmailField()
    description = models.TextField(max_length=300, verbose_name='Company Description')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Company Name:{self.name};Company Address:{self.address}'


class MedicineProduct(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Serial Number')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_medicine')
    user_info = models.ForeignKey(Admin, on_delete=models.CASCADE)
    name = models.CharField(max_length=300, verbose_name='Medicine Name', null=True)
    m_type = models.CharField(max_length=300, verbose_name='Which type of Medicine', null=True)
    des = models.TextField(max_length=500, verbose_name='Medicine Description', null=True)
    b_no = models.CharField(max_length=100, verbose_name='Batch No', null=True)
    s_no = models.CharField(max_length=100, verbose_name='Shelf No or Rack No', null=True)
    mfg_date = models.DateField(verbose_name='Manufacture Date')
    expire_date = models.DateField(verbose_name='Expire Date')
    dar_no = models.CharField(max_length=300, verbose_name='Combination of Drag Administration Number', null=True)
    mfg_Lic = models.CharField(max_length=300, verbose_name='Manufacturing Licence Number', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    buy_price = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Medicine Name:{self.name};Medicine Type:{self.m_type}'


class Sale(models.Model):
    item = models.ForeignKey(MedicineProduct, on_delete=models.CASCADE)
    user_info = models.ForeignKey(Admin, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    def get_profit(self):
        total = self.unit_price - self.item.buy_price
        return int(total)

    def __str__(self):
        return self.item.name
        
pharmacy_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='medicine_admin', null=True,
                                    blank=True)
    ph_manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='medicine_manager', null=True,
                                      blank=True)
    ph_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='medicine_employee', null=True,
                                       blank=True)


'''


class Company(models.Model):
    id = models.AutoField(primary_key=True)

    pharmacy_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='company_admin', null=True,
                                    blank=True)
    ph_manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='company_manager', null=True,
                                      blank=True)
    ph_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='company_employee', null=True,
                                       blank=True)
    name = models.CharField(max_length=255, verbose_name='Company Name')
    lic_no = models.CharField(max_length=300, verbose_name='License Number')
    address = models.CharField(max_length=300, verbose_name='Company Headquarter Address')
    cont_num = models.CharField(max_length=264, verbose_name='Company Contact Information')
    email = models.EmailField()
    description = models.TextField(max_length=300, verbose_name='Company Description')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Company Name:{self.name};Company Address:{self.address}'


class MedicineProduct(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Serial Number')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_medicine', null=True, blank=True)

    pharmacy_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='medicine_admin', null=True,
                                    blank=True)
    ph_manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='medicine_manager', null=True,
                                      blank=True)
    ph_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='medicine_employee', null=True,
                                       blank=True)
    name = models.CharField(max_length=300, verbose_name='Medicine Name', null=True)
    m_type = models.CharField(max_length=300, verbose_name='Which type of Medicine', null=True)
    des = models.TextField(max_length=500, verbose_name='Medicine Description', null=True)
    b_no = models.CharField(max_length=100, verbose_name='Batch No', null=True)
    s_no = models.CharField(max_length=100, verbose_name='Shelf No or Rack No', null=True)
    mfg_date = models.DateField(verbose_name='Manufacture Date')
    expire_date = models.DateField(verbose_name='Expire Date')
    dar_no = models.CharField(max_length=300, verbose_name='Combination of Drag Administration Number', null=True)
    mfg_Lic = models.CharField(max_length=300, verbose_name='Manufacturing Licence Number', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    buy_price = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Medicine Name:{self.name};Medicine Type:{self.m_type}'


class Sale(models.Model):
    item = models.ForeignKey(MedicineProduct, on_delete=models.CASCADE)

    pharmacy_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='sale_admin', null=True,
                                    blank=True)
    ph_manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='sale_manager', null=True,
                                      blank=True)
    ph_employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sale_employee', null=True,
                                       blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True, verbose_name='Issued To')

    def get_total(self):
        total = self.quantity * self.item.unit_price
        return int(total)

    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))

    def get_profit(self):
        total = self.unit_price - self.item.buy_price
        return int(total)

    def __str__(self):
        return self.item.name
