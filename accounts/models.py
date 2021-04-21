# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime

class Agent(models.Model):
    agent_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    username = models.ForeignKey('Login', models.DO_NOTHING, db_column='username')
    first_name = models.CharField(db_column='first_Name', max_length=32)  # Field name made lowercase.
    last_name = models.CharField(db_column='last_Name', max_length=32)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=32)
    contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'agent'

    def __str__(self):
        return str(self.agent_id)



class BuySellTransaction(models.Model):
    tsnc_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    date = models.DateField()
    property = models.ForeignKey('Property', models.DO_NOTHING)
    buyer = models.ForeignKey('Buyer', models.DO_NOTHING)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    owner = models.ForeignKey('Owner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buy_sell_transaction'
    def __str__(self):
        return str(self.tsnc_id)


class Buyer(models.Model):
    buyer_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'buyer'
    def __str__(self):
        return str(self.buyer_id)





class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'login'
    def __str__(self):
        return str(self.username)


class Owner(models.Model):
    owner_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'owner'
    def __str__(self):
        return str(self.owner_id)


class Property(models.Model):
    STATUS = (
			('On_Lease', 'On_Lease'),
			('for_lease', 'for_lease'),
            ('for_sale', 'for_sale'),
            ('Sold', 'Sold'),
			) 
    TYPE = (
        ('Villa','Villa'),
        ('Cottage','Cottage'),
        ('Bungalow','Bungalow'),
        ('Flat','Flat'),
    )
    property_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    owner = models.ForeignKey(Owner, models.DO_NOTHING)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    pincode = models.DecimalField(max_digits=6, decimal_places=0)
    no_of_bedrooms = models.DecimalField(max_digits=2, decimal_places=0)
    size = models.DecimalField(max_digits=10, decimal_places=0)
    type = models.CharField(max_length=32,choices=TYPE)
    status = models.CharField(max_length=32,choices=STATUS)
    amount = models.DecimalField(max_digits=32, decimal_places=0)
    agent = models.ForeignKey(Agent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'property'
    def __str__(self):
        return str(self.property_id)


class RentTransaction(models.Model):
    tsnc_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    date = models.DateField(blank=True, null=True,default=datetime.date.today)
    property = models.ForeignKey(Property, models.DO_NOTHING)
    tenant = models.ForeignKey('Tenant', models.DO_NOTHING)
    agent = models.ForeignKey(Agent, models.DO_NOTHING)
    owner = models.ForeignKey(Owner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rent_transaction'

    def __str__(self):
        return str(self.tsnc_id)


class Tenant(models.Model):
    tenant_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tenant'
    def __str__(self):
        return str(self.tenant_id)


class User(models.Model):
    user_id = models.DecimalField(primary_key=True, max_digits=16, decimal_places=0)
    username = models.ForeignKey(Login, models.DO_NOTHING, db_column='username')
    first_name = models.CharField(db_column='first_Name', max_length=32)  # Field name made lowercase.
    last_name = models.CharField(db_column='last_Name', max_length=32)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=32)
    contact = models.DecimalField(unique=True, max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'user'
    def __str__(self):
        return str(self.user_id)
