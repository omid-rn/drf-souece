from rest_framework import serializers
from blog.models import Article
from drf_dynamic_fields import DynamicFieldsMixin
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# class AuthorSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = get_user_model()
# 		fields = ["id","username","first_name","last_name"]		

# class AuthorUsernameField(serializers.RelatedField):
# 	def to_representation(self,value):
# 		return value.username
		
class ArticleSerialiser(DynamicFieldsMixin,serializers.ModelSerializer):
	# author = serializers.HyperlinkedIdentityField(view_name = 'api:authors-detail') 
	# author = AuthorUsernameField(read_only = True)
	# author = serializers.CharField(source = "author.username", read_only=True)
	def get_author(self,obj):
		return obj.author.username

	author = serializers.SerializerMethodField("get_author")

	class Meta:
		model = Article
		fields = "__all__"
		# fields = ("title","slug","author","content","publish","status")
		# exclude = ("created","updated")
	def validate_title(self, value):
		filter_list = ["javascript","php"]
		for i in filter_list:
				if i in value:
					raise serializers.ValidationError("Don't use bad words!: {}".format(i))	
class UserSerialiser(serializers.ModelSerializer):
	class Meta:
		# model = User
		model = get_user_model()
		# fields = ("title","slug","author","content","publish","status")
		# exclude = ("created","updated")
		fields = "__all__"		 