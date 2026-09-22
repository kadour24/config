from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .services.project_services import ProjectServices
from .serializers import ProjectSerializer


class ProjectView(APIView):

    @property
    def service(self) :
        return ProjectServices()
    
    def get(self, request, project_id=None):

        if project_id is not None:
            project = self.service.get_project(project_id=project_id)

            serializer = ProjectSerializer(project)

            return Response(serializer.data,status=status.HTTP_200_OK)

        projects = self.service.projects_list()

        serializer = ProjectSerializer(
            projects,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project = self.service.create_project(**serializer.validated_data)

        response_serializer = ProjectSerializer(project)

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )
    
    def patch(self, request, project_id=None):
        if project_id is None:
            return Response(
                {"detail": "project_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        project = self.service.done_project(project_id)

        serializer = ProjectSerializer(project)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

