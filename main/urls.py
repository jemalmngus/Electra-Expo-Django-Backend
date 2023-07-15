from django.urls import path
from .views import TestimonialListAPIView
from .views import FAQListCreateView, FAQRetrieveUpdateDestroyView,SubscribeAPIView,ExhibitorViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'exhibitors', ExhibitorViewSet, basename='exhibitor')

urlpatterns = [
    path('testimonials/', TestimonialListAPIView.as_view(), name='testimonial-list'),
    path('faq/', FAQListCreateView.as_view(), name='faq-list-create'),
    path('faq/<int:pk>/', FAQRetrieveUpdateDestroyView.as_view(), name='faq-retrieve-update-destroy'),
    path('subscribe/', SubscribeAPIView.as_view(), name='subscribe'),
    path('', include(router.urls)),
    
]