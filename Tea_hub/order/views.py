import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .util_views import insert_item
from utility.search_filter import filtering_query
from .serializers import OrderSerializers , OrderDetailSerializers
from .models import OrderModel, OrderDetailModel


class OrderAPI(APIView):

    search_fields = ["order_id"]


def put(request, id):
    data = {}
    try:
        order = OrderModel.objects.filter(pk=id).first()
    except OrderModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = OrderSerializers(order, request.data)
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
        order = OrderModel.objects.filter(order_id__in=del_id["id"])
    except OrderModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = order.update(deleted=1)
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
            order = OrderModel.objects.filter(pk=id, deleted=0)
        else:
            order = OrderModel.objects.filter(deleted=0)

        data["total_record"] = len(order)
        order, data = filtering_query(order, query_string, "order_id", "ORDER")

    except OrderModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serilizer = OrderSerializers(order, many=True)
        data["success"] = True
        data["msg"] = "OK"
        data["data"] = serilizer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    data = {}
    if request.method == "POST":
        order = OrderModel()
        serializer = OrderSerializers(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            if "item" in request.data:
                insert_item(request,serializer.data["order_id"])
            serializer = OrderSerializers(order, many=True)

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
            order = OrderModel.objects.get(pk=id, deleted=0)
        else:
            order = OrderModel.objects.filter(deleted=0)
    except OrderModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        serializer = OrderSerializers(order, request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            if "item" in request.data:
                insert_item(request,serializer.data["order_id"])
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_200_OK)

        data["success"] = False
        data["msg"] = serializer.errors
        data["data"] = []
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailAPI(APIView):

    search_fields = ["order_detail_id"]


def put(request, id):
    data = {}
    try:
        order_detail = OrderDetailModel.objects.filter(pk=id).first()
    except OrderDetailModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = OrderDetailSerializers(order_detail, request.data)
        if serializer.is_valid():
            serializer.save()
            data["success"] = True
            data["msg"] = "Data updated successfully"
            data["data"] = serializer.data
            return Response(data=data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_detail(request):
    data = {}
    del_id = json.loads(request.body.decode("utf-8"))
    if "id" not in del_id:
            data["success"] = False
            data["msg"] = "Record ID not provided"
            data["data"] = []
            return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)
    try:
        order_detail = OrderDetailModel.objects.filter(order_detail_id__in=del_id["id"])
    except OrderDetailModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = order_detail.update(deleted=1)
        data["success"] = True
        data["msg"] = "Data deleted successfully."
        data["deleted"] = result
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_detail(request, id=None):
    query_string = request.query_params
    data = {}
    try:
        if id:
            order_detail = OrderDetailModel.objects.filter(pk=id, deleted=0)
        else:
            order_detail = OrderDetailModel.objects.filter(deleted=0)

        data["total_record"] = len(order_detail)
        order_detail, data = filtering_query(order_detail, query_string, "order_detail_id", "ORDERDETAIL")

    except OrderDetailModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serilizer = OrderDetailSerializers(order_detail, many=True)
        data["success"] = True
        data["msg"] = "OK"
        data["data"] = serilizer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_detail(request):
    data = {}
    if request.method == "POST":
        order_detail = OrderDetailModel()
        serializer = OrderDetailSerializers(order_detail, data=request.data)

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
def patch_detail(request, id):
    data = {}

    try:
        if id:
            order_detail = OrderDetailModel.objects.get(pk=id, deleted=0)
        else:
            order_detail = OrderDetailModel.objects.filter(deleted=0)
    except OrderDetailModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        serializer = OrderDetailSerializers(order_detail, request.data, partial=True)

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



