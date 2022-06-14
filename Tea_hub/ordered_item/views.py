import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from utility.search_filter import filtering_query
from .serializers import OrderedItemsSerializers
from .models import OrderedItemsModel


class OrderedItemsAPI(APIView):

    search_fields = ["ordered_items_id"]


def put(self, request, id):
    data = {}
    try:
        ordered_items = OrderedItemsModel.objects.filter(pk=id).first()
    except OrderedItemsModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "PUT":
        serializer = OrderedItemsSerializers(ordered_items, request.data)
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
        ordered_items = OrderedItemsModel.objects.filter(ordered_items_id__in=del_id["id"])
    except OrderedItemsModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "DELETE":
        result = ordered_items.update(deleted=1)
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
            ordered_items = OrderedItemsModel.objects.filter(pk=id, deleted=0)
        else:
            ordered_items = OrderedItemsModel.objects.filter(Q(deleted=0, created_by=1)  | Q(created_by=request.data.get('created_by')))

        data["total_record"] = len(ordered_items)
        ordered_items, data = filtering_query(ordered_items, query_string, "ordered_items_id", "ORDEREDITEMS")

    except OrderedItemsModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "GET":
        serilizer = OrderedItemsSerializers(ordered_items, many=True)
        data["success"] = True
        data["msg"] = "OK"
        data["data"] = serilizer.data
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create(request):
    data = {}
    if request.method == "POST":
        ordered_items = OrderedItemsModel()
        serializer = OrderedItemsSerializers(ordered_items, data=request.data)

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
            ordered_items = OrderedItemsModel.objects.get(pk=id, deleted=0)
        else:
            ordered_items = OrderedItemsModel.objects.filter(deleted=0)
    except OrderedItemsModel.DoesNotExist:
        data["success"] = False
        data["msg"] = "Record Does not exist"
        data["data"] = []
        return Response(data=data, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == "POST":
        serializer = OrderedItemsSerializers(ordered_items, request.data, partial=True)

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



