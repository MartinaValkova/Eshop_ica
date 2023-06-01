from django.db import models



# Create your models here.

#Database for products done by Martina
class Product(models.Model):
    
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

#Database for Order done by Martina

class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

# Database for Contact details done by Jeremy

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return 'Message from {self.name}'
    


#Database for Order done by Alibay

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Define a one-to-one relationship with the User model

#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     # Define an ImageField to store the profile picture, with a default image and upload path

#     def __str__(self):
#         return f'{self.user.username} Profile'
#         # Return a string representation of the profile, using the username of the associated user

#     def save(self):
#         super().save()
#         # Call the save() method of the parent class

#         img = Image.open(self.image.path)
#         # Open the image file using the PIL library

#         if img.height > 300 or img.width > 300:
#             # Check if the image is larger than the specified size
#             output_size = (300, 300)
#             # Define the desired output size
#             img.thumbnail(output_size)
#             # Resize the image to fit within the specified size while maintaining aspect ratio
#             img.save(self.image.path)
#             # Save the modified image back to the original path