from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TemperatureSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from .utils import TemperatureCalculator

temperature = TemperatureCalculator()

@api_view(['GET'])
def test(request):
    return Response({"Server Status" : "ok"}, status=status.HTTP_200_OK)


class TemperatureViews(APIView):
    """
        GET: NOT
    """

    parser_classes = [FormParser, MultiPartParser]
    serializer_class = TemperatureSerializer

    def post(self, request):
        serializer_data = self.serializer_class(data=request.data)
        if serializer_data.is_valid():
            degrees = serializer_data.validated_data['degrees']
            from_ = serializer_data.validated_data['from_']
            to_ = serializer_data.validated_data['to_']
            result = temperature.convert_temperature(degrees, from_, to_)
            result_round = round(result, 2)
            response = {
                from_: degrees,
                'from_': from_,
                'to_': to_,
                to_: result,
                'result': result,
                f'round_{to_}': result_round,
                'message': f'{from_}: {degrees} and {to_} is {result} ({result_round})'
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response({'errors': serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class TimeView(APIView):
    
    def post(self, request):
        pass