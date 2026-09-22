from ..models import Project
from django.shortcuts import get_object_or_404

class ProjectServices :

    def projects_list(self) :
        return Project.objects.all()
    
    def get_project(self, project_id) :
        return get_object_or_404(
            Project, id = project_id
        )
    
    def delete_project(self, project_id) :
        project = get_object_or_404(Project,id=project_id) 
        project.delete()
    
    def create_project(self, **data):
        return Project.objects.create(**data)

    def done_project(self,project_id) :
        project = get_object_or_404(Project,id=project_id)
        project.progress = "DONE"
        project.save()
        return project
    