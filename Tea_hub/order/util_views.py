from order.models import OrderDetailModel
from order.serializers import OrderDetailSerializers


def insert_item(request, order_id):
    OrderDetailModel.objects.filter(order_id=order_id).delete()

    if "item" in request.data:
        item_list = request.data.get('item')  

        item_dict = {}
        for item1 in item_list:
            item_dict["item"] = item1["item"]
            item_dict["quantity"] = item1["quantity"]
            item_dict["rate"] = item1["rate"]
            item_dict["order"] = order_id
            item_dict["created_by"] = request.data.get('created_by')

            item = OrderDetailModel()
            serializer = OrderDetailSerializers(item, data=item_dict)

            if serializer.is_valid():
                serializer.save()
