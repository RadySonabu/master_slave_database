from django.urls import path, include
from rest_framework import routers
from .views import Contact_A00View, Contact_A01View, Contact_A02View, Group_A00View, Group_A01View

router = routers.DefaultRouter()
router.register('contact', Contact_A00View)
router.register('contact-detail', Contact_A01View)
router.register('contact-endorsement', Contact_A02View)
router.register('group', Group_A00View)
router.register('group-detail', Group_A01View)


urlpatterns = [
    path('api/', include(router.urls)),
    # path('', views.home, name='home')

]
