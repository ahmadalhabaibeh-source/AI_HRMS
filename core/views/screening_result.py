
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import ScreeningResult
from ..serializers import ScreeningResultSerializer


class ScreeningResultDetailAPIView(APIView):

    def get(self, request, pk):

        screening_result = get_object_or_404(
            ScreeningResult,
            pk=pk
        )

        serializer = ScreeningResultSerializer(
            screening_result
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
