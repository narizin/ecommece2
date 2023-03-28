from django.shortcuts import render
from rest_framework.response import Response
from  rest_framework.renderers import TamplateHTMLRenderer
from rest_framework.views import APIView

class IndexPage(APIView):
    renderer_classes = [TamplateHTMLRenderer]
    template_name = 'page/index.html'

    def get_(self, request):
        return Response({})


