from django.shortcuts import render
from rest_framework.generics import ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,CreateAPIView
from .serializers import AccountListSerializer,AccountUpdateSerializer,AccountDetailSerializer,AccountCreateSerializer
from .models import Account

class AccountList(ListAPIView):
    queryset=Account.objects.all()
    serializer_class= AccountListSerializer

class AccountUpdate(UpdateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountUpdateSerializer
    lookup_url_kwarg = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    # def patch(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.partial_update(request, *args, **kwargs)


class AccountDelete(DestroyAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountDetailSerializer
    lookup_url_kwarg = "id"

class AccountCreate(CreateAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountCreateSerializer

class AccountDetail(RetrieveAPIView):
    queryset=Account.objects.all()
    serializer_class=AccountDetailSerializer

