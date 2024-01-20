from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from company.filters import CompanyFilter
from company.models import Company
from company.permissions import IsActiveEmployee
from company.serliazers import CompanySerializer, CompanyDetailSerializer


class CompanyCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания компании"""
    serializer_class = CompanyDetailSerializer
    permission_classes = [IsActiveEmployee]


class CompanyListAPIView(generics.ListAPIView):
    """Эндпоинт просмотра списка компаний"""
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter
    permission_classes = [IsActiveEmployee]


class CompanyRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра компании"""
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]


class CompanyUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт редактирования компании"""
    serializer_class = CompanyDetailSerializer
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]

    def perform_update(self, serializer):
        """
        Обрабатывает операцию обновления для объекта Company.
        При обновлении объекта поле 'debt' не изменяется
        и сохраняет свое первоначальное значение.
        """
        serializer.save(debt=self.get_object().debt)


class CompanyDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления компании"""
    queryset = Company.objects.all()
    permission_classes = [IsActiveEmployee]
