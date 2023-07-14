from django.contrib import admin
from .models import FAQ,Subscription,Testimonial

admin.site.site_header = "Electric Expo Admin"
admin.site.site_title = "Electric Expo Admin"
admin.site.index_title = "Dashboard"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


admin.site.register(FAQ)
admin.site.register(Subscription)
