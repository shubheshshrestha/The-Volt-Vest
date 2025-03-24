from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from customers.models import CustomerProfile

User = get_user_model()

from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
from customers.models import CustomerProfile

User = get_user_model()

class Order(models.Model):
    STATUS_CHOICES = {
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned')
    }
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product, through='OrderProduct')  # Relate products directly
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def calculate_total_price(self):
        return sum(op.product.price * op.quantity for op in self.orderproduct_set.all())

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()

    @property
    def subtotal(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together = ('order', 'product')  # Prevent duplicate product entries per order


# class Order(models.Model):
#     STATUS_CHOICES = {
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#         ('returned', 'Returned')
#     }
#     customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) # Total price of the order
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     def calculate_total_price(self):
#         return sum(item.subtotal for item in self.order_items.all())

#     def save(self, *args, **kwargs):
#         # super().save(*args, **kwargs)
#         # self.total_price = self.calculate_total_price()
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"Order #{self.id} by {self.customer}"

# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     @property
#     def subtotal(self):
#         return self.price * self.quantity

    # def save(self, *args, **kwargs):
    #     if not self.price:  # Set price if not provided or 0
    #         self.price = self.product.price
    #     super().save(*args, **kwargs)

# from django.db import models
# from django.contrib.auth import get_user_model 
# from products.models import Product
# from customers.models import CustomerProfile

# # Create your models here.

# User = get_user_model()

# class Order(models.Model):    # Model to store order info
#     STATUS_CHOICES = {        # Status of the order  
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('delivered', 'Delivered'),
#         ('cancelled', 'Cancelled'),
#         ('returned', 'Returned')
#     }   
#     customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders') # Foreign key to the customer who placed the order
#     # products = models.ManyToManyField(Product) # ManyToMany relationship to products
#     # quantity = models.PositiveIntegerField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)

#     def calculate_total_price(self):
#         return sum(product.price for product in self.products.all())    # Method to calculate total price based on order items

#     # Override save method to automatically calculate total price
#     def save(self, *args, **kwargs):
#         # Auto calculate total price when saving
#         # self.total_price = self.product.price * self.quantity
#         self.total_price = self.calculate_total_price()
#         super().save(*args, **kwargs)         

#     # String representative of the order
#     def __str__(self):
#         return f"Order #{self.id} by {self.customer}"
    
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     @property
#     def subtotal(self):
#         return self.price * self.quantity

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.price = self.product.price
#         super().save(*args, **kwargs)
#         super().save(*args, **kwargs)

# # class OrderItem(models.Model):      # to store individual products in an order
# #     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
# #     product = models.ForeignKey(Product, on_delete=models.PROTECT)
# #     quantity = models.PositiveIntegerField() # Quantity of the product ordered
# #     price = models.DecimalField(max_digits=10, decimal_places=2) # Price of the product at the time of purchase

# #     # Property to calculate subtotal for this item
# #     @property
# #     def subtotal(self):
# #         return self.price * self.quantity
    
# #     # Override save method to automatically set price from product
# #     def save(self, *args, **kwargs):
# #         if not self.pk:
# #             self.price = self.product.price
# #         super().save(*args, **kwargs)