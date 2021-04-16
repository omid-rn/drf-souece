# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.
# class ArticleList(ListCreateAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerialiser

# class ArticleDetail(RetrieveUpdateDestroyAPIView):
# 	queryset = Article.objects.all()
# 	serializer_class = ArticleSerialiser
# 	#  lookup_field = "slug"
# 	permission_classes = (IsAuthorOrReadOnly,)

class ArticleViewSet(ModelViewSet):
	serializer_class = ArticleSerialiser
	queryset = Article.objects.all()
	filterset_fields = ["status","author__username"]
	ordering_fields = ['publish', 'status']
	ordering = ['-publish']
	search_fields = ["title","content","author__username","author__first_name","author__last_name"]
	# def get_queryset(self):

	# 	status = self.request.query_params.get('status')
	# 	if status is not None:
	# 		queryset = queryset.filter(status = status)
	# 	return queryset	

	# 	author = self.request.query_params.get('author')
	# 	if author is not None:
	# 		queryset = queryset.filter(author__username = author)
	# 	return queryset	
			
	def get_permissions(self):
	    if self.action == ['list','create']:
	        permission_classes = [IsStaffOrReadOnly]
	    else:
	        permission_classes = [IsStaffOrReadOnly,IsAuthorOrReadOnly]
	    return [permission() for permission in permission_classes]


# class UserList(ListCreateAPIView):
# 	# def get_queryset(self):
# 	# 	print("------------------------")
# 	# 	print(self.request.user)
# 	# 	print(self.request.auth)
# 	# 	print("------------------------")
# 	queryset = User.objects.all()
# 	serializer_class = UserSerialiser
# 	permission_classes=(IsSuperUserOrStaffReadOnly,)

# class UserDetail(RetrieveUpdateDestroyAPIView):
# 	def get_queryset(self):
# 		self.request.auth.delete()
# 		return User.objects.all()
# 	queryset = User.objects.all()
# 	serializer_class = UserSerialiser
# 	permission_classes=(IsSuperUserOrStaffReadOnly,)	

# class RevokeToken(APIView):
# 	permission_classes	 = (IsAuthenticated,)

# 	def get(self,request):
# 		return Response({"method" : "get"})

	
# 	def post(self,request):
# 		return Response({"method" : "post"})
	
# 	def put(self,request):
# 		return Response({"method" : "put"})

	
# 	def delete(self,request):
# 		request.auth.delete()
# 		return Response(status=204)			

class UserViewSet(ModelViewSet):
	# queryset = User.objects.all()
	queryset = get_user_model().objects.all()
	serializer_class = UserSerialiser
	permission_classes=(IsSuperUserOrStaffReadOnly,)

# class AuthorRetrieve(RetrieveAPIView):
# 	# queryset = User.objects.all()
# 	queryset = get_user_model().objects.filter(is_staff=True)
# 	serializer_class = AuthorSerializer
