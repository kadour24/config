from rest_framework import serializers
from .models import Project , User

class ProjectSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Project
        fields = [
           "id", "name","project_url", "progress", "descriptions"
        ] 