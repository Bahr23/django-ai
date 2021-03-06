from django.urls import include, path
from rest_framework import routers
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('predict/', views.Predict.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]