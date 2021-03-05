from rest_framework import routers

from .api import *

router = routers.DefaultRouter()
router.register('api/group', GroupViewSet, 'group')
router.register('api/task', TaskViewSet, 'task')
router.register('api/point', PointViewSet, 'point')


urlpatterns = router.urls
