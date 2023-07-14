from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Testimonial, FAQ, Subscription
from .serializers import TestimonialSerializer, FAQSerializer, SubscriptionSerializer
from django.http import HttpResponseForbidden
from django.conf import settings

API_KEY = settings.API_KEY

def validate_api_key(view_func):
    def wrapper(self, request, *args, **kwargs):
        api_key = request.META.get('HTTP_X_API_KEY')
        if api_key != API_KEY:
            return HttpResponseForbidden('Invalid API key')
        return view_func(self, request, *args, **kwargs)
    return wrapper


class SubscribeAPIView(APIView):
    @validate_api_key
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        email = request.data.get('email')  # Get the email from the request data
       
        # Check if the email is already subscribed
        if email and Subscription.objects.filter(email=email).exists():
            return Response({'message': 'Already subscribed'}, status=status.HTTP_409_CONFLICT)
        
        if serializer.is_valid():
            # Create a new subscription
            subscription = serializer.save()
            return Response({'message': 'Subscription successful', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response({'message': 'Validation Error', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class TestimonialListAPIView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
