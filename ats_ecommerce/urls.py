from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView, ContactUsPageView

urlpatterns = [
                  path('adm1800216/', admin.site.urls),
                  path('accounts/', include('accounts.urls', namespace="accounts")),
                  path('store/', include('store.urls', namespace="store")),
                  path('cart/', include('carts.urls', namespace="carts")),
                  path('orders/', include('orders.urls', namespace="orders")),
                  path('', HomePageView.as_view(), name='home'),
                  path('contact/', ContactUsPageView.as_view(), name="contact")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "ats_ecommerce.views.page_not_found_view"
