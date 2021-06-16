from about.models import Contact
from about.serializers import ContactSerializer
from rest_framework.viewsets import ModelViewSet



class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'field'