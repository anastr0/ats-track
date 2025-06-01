from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .models import Candidate
from .serializers import CandidateSerializer

class CandidateViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=False, methods=['POST'], name='Search Candidate')
    def search(self, request, *args, **kwargs):
        search_results = Candidate.objects.filter(name__icontains=request.data['name'])
        serializer = self.get_serializer(search_results, many=True)
        return Response(serializer.data, status=200)
