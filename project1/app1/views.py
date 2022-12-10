from rest_framework import generics, status
import pandas as pd
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer, FileUploadSerializer, SignUpSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q


class SignUpAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


# To upload cvs file
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            print(row[2])
            new_file = Data(
                order_date=row['order_date'],
                region=row['region'],
                manager=row['manager'],
                salesman=row['salesman'],
                items=row['items'],
                units=row['units']

            )
            new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)

# To get all the data


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# To Get perticular Data form particular region
class NewDataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.filter(region='East')
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# To Get perticular Data form particular region and Manager
class PerDataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.filter(Q(region='East') | Q(manager='Martha'))
    serializer_class = DataSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
