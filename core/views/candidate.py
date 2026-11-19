
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import CandidateSerializer


class CandidateCreateAPIView(APIView):

    def post(self, request):

        serializer = CandidateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
