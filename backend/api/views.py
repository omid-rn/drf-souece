# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article
from .serializers import ArticleSerialiser, UserSerialiser
from django.contrib.auth.models import User


# Create your views here.
class ArticleList(ListCreateAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser

class ArticleDetail(RetrieveUpdateDestroyAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerialiser
	#  lookup_field = "slug"
	permission_classes = (IsAuthorOrReadOnly,)

class UserList(ListCreateAPIView):
	# def get_queryset(self):
	# 	print("------------------------")
	# 	print(self.request.user)
	# 	print(self.request.auth)
	# 	print("------------------------")
	queryset = User.objects.all()
	serializer_class = UserSerialiser
	permission_classes=(IsSuperUserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
	def get_queryset(self):
		self.request.auth.delete()
		return User.objects.all()
	queryset = User.objects.all()
	serializer_class = UserSerialiser
	permission_classes=(IsSuperUserOrStaffReadOnly,)	

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