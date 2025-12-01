from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team, TeamMember
from .serializers import TeamSerializer, TeamMemberSerializer
from django.http import Http404

class TeamList(APIView):

    def get(self, request, format= None):
        teams = TeamMember.objects.all()
        serializer = TeamSerializer(teams, many = True)
        return Response(serializer.data)

    def post(self, request, format= None):
        serializer =TeamSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamDetail(APIView):

    def getObject(self, pk):
        try:
            return TeamMember.objects.get(pk = pk)
        except TeamMember.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format= None):
        team = self.getObject(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        team = self.getObject(pk)
        serializer = TeamSerializer(team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        team = self.getObject(pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamMemberList(APIView):

    def get(self, request, format= None):
        teamMembers = Team.objects.all()
        serializer = TeamMemberSerializer(teamMembers, many = True)
        return Response(serializer.data)

    def post(self, request, format= None):
        serializer = TeamMemberSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamMemberDetail(APIView):

    def getObject(self, pk):
        try:
            return TeamMember.objects.get(pk = pk)
        except TeamMember.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format= None):
        teamMembers = self.getObject(pk)
        serializer = TeamSerializer(teamMembers)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        teamMembers = self.getObject(pk)
        serializer = TeamMemberSerializer(teamMembers, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        teamMembers = self.getObject(pk)
        teamMembers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)