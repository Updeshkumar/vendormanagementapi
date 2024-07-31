# vendors/urls.py
from django.urls import path
from .views import vendor_list_create, vendor_detail_update_delete, purchase_order_list_create, purchase_order_detail_update_delete, vendor_performance, acknowledge_purchase_order

urlpatterns = [
    path('vendors/', vendor_list_create, name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', vendor_detail_update_delete, name='vendor-detail-update-delete'),
    path('vendors/<int:vendor_id>/performance/', vendor_performance, name='vendor-performance'),

    path('purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('purchase_orders/<int:po_id>/', purchase_order_detail_update_delete, name='purchase-order-detail-update-delete'),
    path('purchase_orders/<int:po_id>/acknowledge/', acknowledge_purchase_order, name='purchase-order-acknowledge'),
]
