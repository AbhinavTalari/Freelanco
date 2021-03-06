from django.conf import settings
from django.db import models

from users.models import FreelancerProfile, CustomerProfile

class Item(models.Model):
	"""
	An Item is added by the freelancer and has multiple fields like cost, title, description etc
	Only one instance of this should exist in the database.
	"""
	title = models.CharField(max_length=100)
	actual_cost = models.FloatField()
	discounted_cost = models.FloatField(default = -1)
	provider = models.ForeignKey(FreelancerProfile, on_delete = models.CASCADE,related_name="items")
	post_date = models.DateField(null=True,blank=True,auto_now_add=True)
	picture = models.ImageField(default = 'items/default.jpg', upload_to = 'items/uploads')
	active=models.BooleanField(default=True)

	CATEGORY_LIST =[
		('MASSAGE', 'Massage'),
		('SALON', 'Salon'),
		('AC', 'AC Repair'),
		('CLEANING', 'Cleaning'),
		('ELECTRICIAN', 'Electrician'),
		('PLUMBER', 'Plumber'),
		('FITNESS', 'Fitness'),
		('MISCELLANEOUS','Misc')
	]
	category = models.CharField(max_length = 255,
		choices = CATEGORY_LIST,
		default = None
		)

	description = models.TextField()
	def __str__(self):
		return self.title

class OrderItem(models.Model):
	"""
	An OrderItem instance would be in an ongoing order, a past order or an order that hasn't been placed.
	This model is there to prevent making multiple copies of Item model and remove redundancy.
	"""
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	ordered = models.BooleanField(default=False)
	user = models.ForeignKey(CustomerProfile,
								on_delete=models.CASCADE)
	accepted = models.IntegerField(default = 3)
		# 0 for pending approval
		# 1 for accepted
		# 2 for rejected
	status = models.IntegerField(default = 2)
		# 0 for ongoing
		# 1 for done
		# 2 not started

	def __str__(self):
		return self.item.title



class Order(models.Model):
	"""
	Each order has order items and hence the relation field 'items'. An order is also
	a representation of a cart provided that the order hasn't been placed.
	"""
	user = models.ForeignKey(CustomerProfile,
								on_delete=models.CASCADE)

	items = models.ManyToManyField(OrderItem)
	# Cart creation time
	start_date = models.DateTimeField(auto_now_add=True)
	# Order time
	ordered_date = models.DateTimeField(null=True, blank = True)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.user.username+"order"
