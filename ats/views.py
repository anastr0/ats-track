from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        # partial update by default
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=["POST"], name="Search Candidate")
    def search(self, request, *args, **kwargs):
        # validate request has input 'name'
        if not request.data.get("name"):
            return Response({"error": "Name is required"}, status=400)

        # perform search
        search_results = Candidate.search_name(request.data["name"])

        # if no results, return 404
        if search_results.count() == 0:
            return Response({"info": "No candidates found"}, status=204)

        serializer = self.get_serializer(search_results, many=True)
        return Response(serializer.data, status=200)
