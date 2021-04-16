from django.urls import path, include
# from .views import ArticleList, ArticleDetail, UserList,UserDetail
from .views import UserViewSet, ArticleViewSet
from rest_framework import routers
# urlpatterns = [
# 	path("",ArticleList.as_view(), name="list"),
# 	path("<int:pk>",ArticleDetail.as_view(), name="detail"),
# 	path("users/",UserList.as_view(), name="user-list"),
# 	path("users/<int:pk>",UserDetail.as_view(), name="user-detail"),
# ] 

app_name = "api"

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet,basename = "articles")
router.register('users', UserViewSet,basename = "users")
# urlpatterns = router.urls

urlpatterns = [
	path("",include(router.urls)),
	# path("authors/<int:pk>/",AuthorRetrieve.as_view(), name="authors-detail")



]