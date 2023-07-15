from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Exhibitor(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.company_name

