from ..models import Project
from django.shortcut import get_object_or_404

class ProjectServices :

    def projects_list() :
        return Project.objects.filter(progress="TODO").all()
    
    def get_project(self, project_id) :
        return get_object_or_404(
            Project, id = project_id
        )
    
    def delete_project(self, project_id) :
        project = get_object_or_404(Project,id=project_id) 
        project.delete()
    
    