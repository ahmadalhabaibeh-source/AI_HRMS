
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import InterviewQuestionSet
from ..serializers import InterviewQuestionSetSerializer



class InterviewQuestionSetDetailAPIView(APIView):

    def get(self, request, pk):

        interview_questions = get_object_or_404(
            InterviewQuestionSet,
            pk=pk
        )

        serializer = InterviewQuestionSetSerializer(
            interview_questions
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
