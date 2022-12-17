from django.urls import path

from products.views import ProductsView, ProductDetail, export_csv,\
     import_csv, ExportPDF, favorites, product_favorite_list, products

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    # path('products/', products, name='products'),
    path('products/<uuid:pk>/', ProductDetail.as_view(),
         name='product_detail'),
    path('products/csv/', export_csv, name='export_csv'),
    path('products/pdf/', ExportPDF.as_view(), name='export_pdf'),
    path('products/import/', import_csv, name='import_csv'),
    path('favorites/', product_favorite_list, name='favorites'),
    path('favorites/<uuid:product_id>/', favorites,
         name='add_or_remove_favorite'),
]

