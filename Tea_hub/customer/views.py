import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from utility.search_filter import filtering_query
from .serializers import CustomerSerializers
from .models import CustomerModel


class CustomerAPI(APIView):

    search_fields = ["customer_id"]


def put(self, request, id):
    data = {}
    try:
        customer = CustomerModel.objects.filter(pk=id).first()
    except CustomerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = CustomerSerializers(customer, request.data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request):
    data = {}
    del_id = json.loads(request.body.decode("utf-8"))
    if "id" not in del_id:
            data["success"] = False
            data["msg"] = "Record ID not provided"
            data["data"] = []
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    try:
        customer = CustomerModel.objects.filter(customer_id__in=del_id["id"])
    except CustomerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = customer.update(deleted=1)
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
            customer = CustomerModel.objects.filter(pk=id, deleted=0)
        else:
            customer = CustomerModel.objects.filter(deleted=0)

        data["total_record"] = len(customer)
        customer, data = filtering_query(customer, query_string, "customer_id", "CUSTOMER")

    except CustomerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serilizer = CustomerSerializers(customer, many=True)
        data["success"] = True
        data["msg"] = "OK"
        data["data"] = serilizer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    data = {}
    if request.method == "POST":
        customer = CustomerModel()
        serializer = CustomerSerializers(customer, data=request.data)

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
            customer = CustomerModel.objects.get(pk=id, deleted=0)
        else:
            customer = CustomerModel.objects.filter(deleted=0)
    except CustomerModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        serializer = CustomerSerializers(customer, request.data, partial=True)

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



