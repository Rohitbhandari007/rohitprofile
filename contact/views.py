from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings



class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        name = request.data.get('name')
        email = request.data.get('email')
        messege = request.data.get('messege')
        email_host = "rohitportfolioemailsender@gmail.com"
        if serializer.is_valid():
            serializer.save()

            send_mail(name, "Your messege [" + messege + "] has been received", email_host, [email,'rohitbhandari20561210@gmail.com', ])

            return Response(serializer.data)
        return Response(serializer.errors)

def index(request):
    return render(request, 'contact/index.html')
#init