from django.contrib import admin
from django.urls import path
from blog import views   # 👈 IMPORTANT
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('post/<int:id>/', views.post_detail),# 👈 THIS MUST POINT TO BLOG

    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)