from rest_framework import viewsets, permissions
from leads.models import Leads
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer