from rest_framework import serializers
from . import models
class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectCategory
        fields = "__all__"
        depth = 1


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Projects
        fields = "__all__"
        depth = 1
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = "__all__"
        depth = 1
        
        
class MyselfSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Myself
        fields = "__all__"
        depth = 1
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = "__all__"
        depth = 1
        
class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tools
        fields = "__all__"
        depth = 1

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Resume
        fields = "__all__"
        depth = 1
class ResumeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResumeCategory
        fields = "__all__"
        depth = 1
