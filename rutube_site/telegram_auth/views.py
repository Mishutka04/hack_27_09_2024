from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Code

class AuthTelegramAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        code = request.data['code']
        data = Code.objects.filter(code = code)[0]
        if not data:
            return Response(
            {
                'error': 'Code not find'
            } 
            )
        Code.objects.filter(code = code).delete()
        Code.objects.create(user = request.user,user_id =  data.user_id, chat_id = data.chat_id)
        return Response(
            {
                'authentication': 'It was successful'
            } )
            

# Create your views here.
