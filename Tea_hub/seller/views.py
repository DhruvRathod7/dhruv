from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from utility.search_filter import filtering_query
from .serializers import SellerSerializers
from .models import SellerModel


class SellerAPI(APIView):

    search_fields = ["seller_id"]


def put(self, request, id):
    data = {}
    try:
        seller = SellerModel.objects.filter(pk=id).first()
    except SellerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = SellerSerializers(seller, request.data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, id):
    data = {}
    try:
        seller = SellerModel.objects.filter(pk=id)
    except SellerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = seller.update(deleted=1)
        data["success"] = True
        data["msg"] = "Data deleted successfully."
        data["deleted"] = result
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get(request, id=None):
    query_string = request.query_params
    data = {}
    try:
        if id:
            seller = SellerModel.objects.filter(pk=id, deleted=0)
        else:
            seller = SellerModel.objects.filter(deleted=0)

        data["total_record"] = len(seller)
        seller, data = filtering_query(seller, query_string, "seller_id", "SELLER")

    except SellerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serilizer = SellerSerializers(seller, many=True)
        data["success"] = True
        data["msg"] = "OK"
        data["data"] = serilizer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    data = {}
    if request.method == "POST":
        seller = SellerModel()
        serializer = SellerSerializers(seller, data=request.data)

        if serializer.is_valid():
            serializer.save()
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_201_CREATED)

        data["success"] = False
        data["msg"] = serializer.errors
        data["data"] = serializer.data
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

# ===========================update=================================================


@api_view(['POST'])
def patch(request, id):
    data = {}

    try:
        if id:
            seller = SellerModel.objects.get(pk=id, deleted=0)
        else:
            seller = SellerModel.objects.filter(deleted=0)
    except SellerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        serializer = SellerSerializers(seller, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_200_OK)

        data["success"] = False
        data["msg"] = serializer.errors
        data["data"] = []
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



