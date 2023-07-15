from rest_framework import serializers

from .models import Testimonial,Subscription,FAQ,Exhibitor


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
        # permission_classes = [AllowAny]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('email',)
class ExhibitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibitor
        fields = ['id', 'company_name', 'name', 'email', 'contact_number']