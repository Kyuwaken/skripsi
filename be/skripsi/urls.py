"""skripsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import viewsets
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'cart', viewsets.CartViewSet)
router.register(r'category', viewsets.CategoryViewSet)
router.register(r'country', viewsets.CountryViewSet)
router.register(r'courier', viewsets.CourierViewSet)
router.register(r'favorite', viewsets.FavoriteViewSet)
router.register(r'master_status', viewsets.MasterStatusViewSet)
router.register(r'payment_method', viewsets.PaymentMethodViewSet)
router.register(r'payment_type', viewsets.PaymentTypeViewSet)
router.register(r'payment', viewsets.PaymentViewSet)
router.register(r'product_review', viewsets.ProductReviewViewSet)
router.register(r'product', viewsets.ProductViewSet)
router.register(r'transaction_detail', viewsets.TransactionDetailViewSet)
router.register(r'transaction_status', viewsets.TransactionStatusViewSet)
router.register(r'transaction', viewsets.TransactionViewSet)
router.register(r'product-image', viewsets.ProductImageViewSet)
router.register(r'user', viewsets.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', viewsets.LoginView.as_view()),
    path('logout/', viewsets.LogoutView.as_view()),
    path('login/user/', viewsets.LoginUserView.as_view()), # for checking role
    path('', include(router.urls)),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)