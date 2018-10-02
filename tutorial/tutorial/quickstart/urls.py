from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# from rest_framework.authtoken import views1 

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += [
     url(r'^api-token-auth/', views.CustomAuthToken.as_view())
    # url(r'^api-token-auth/', views.obtain_auth_token)
]