from django.contrib import admin
from django.urls import path
from basic_app import views
from django.conf.urls import url, include

# template urls

app_name = 'basic_app'

urlpatterns=[
    url(r'^$',views.MenuListView.as_view(),name='list'),
    path('<int:pk>/', views.MenuDetailView.as_view(), name='detail'),
    path('<int:pk>/', views.MenuUpdateView.as_view(), name='update'),
    url(r'^create/$',views.MenuCreateView.as_view(),name='create'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^payments/$', views.payments, name='payments')

]


"""
urlpatterns = [
    path('', views.IndexView.as_view()),
    path('admin/', admin.site.urls),
    path('basic_app/', include('basic_app.urls', namespace='basic_app')),
]
"""