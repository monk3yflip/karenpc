"""
Definition of urls for Lab4.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('product/<int:product_id>/', views.product_view, name='product'),
    path('order/', views.order_view, name='order'),
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('anketa/', views.anketa, name='anketa'),
    path('blog/', views.blog, name='blog'),

    path('blogpost/<int:parametr>/', views.blogpost, name='blogpost'),
    path('registration/', views.registration, name='registration'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
