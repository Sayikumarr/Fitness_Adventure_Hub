from django.conf import settings
from django.contrib import admin
from django.urls import path
from admin_portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact', views.contactForm),
    path('blog/<int:pk>', views.blogpost),
]


from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)