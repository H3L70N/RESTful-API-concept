from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer)
        # serializer.save()

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title
        serializer.save(content=content)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # stuff
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     # lookup_field = 'pk'
#
#
# product_list_view = ProductListAPIView.as_view()
#
# class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def get(self, request, *args, **kwargs):
#         print(args, kwargs)
#         pk = kwargs.get('pk')
#
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#
#         return self.create(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         # print(serializer)
#         # serializer.save()
#
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#
#         if content is None:
#             content = "Testing mixin"
#         serializer.save(content=content)
#
#
# product_mixin_view = ProductMixinView.as_view()
#
#
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method
#
#     if method == "GET":
#         if pk is not None:
#             # detail_view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#
#         # list_ view
#         query_set = Product.objects.all()
#         data = ProductSerializer(query_set, many=True).data
#         return Response(data)
#
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#
#         if serializer.is_valid():
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             print(serializer.data)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)
