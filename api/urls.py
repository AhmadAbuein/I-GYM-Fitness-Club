from rest_framework import routers
from .views import MemberViewSet, MembershipViewSet
from django.urls import path
# from .views import member_list, member_detail




router = routers.DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'memberships', MembershipViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('members/', member_list),
#     path('members/<int:pk>/', member_detail),
    
# ]