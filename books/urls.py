from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('', BookViewSet, basename = 'books')
router.register('authors', AuthorViewSet, basename = 'authors')


urlpatterns = router.urls