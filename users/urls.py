from django.urls import path
from .views import RegisterView, LoginView
from .views import book_list
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('books/', book_list, name='book-list'),
]
