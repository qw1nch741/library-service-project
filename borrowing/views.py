from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from borrowings.models import Borrowing
from borrowings.serializers import (
    BorrowingReadSerializer,
    BorrowingCreateSerializer,
)

class BorrowingViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    # We require users to be logged in to interact with borrowings
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Borrowing.objects.all()
        user = self.request.user

        # 1. Enforce the Customer vs Admin visibility rule
        if not user.is_staff:
            queryset = queryset.filter(user=user)
        else:
            # Admins can optionally filter by a specific user_id in the URL
            user_id = self.request.query_params.get("user_id")
            if user_id:
                queryset = queryset.filter(user_id=user_id)

        # 2. Handle the ?is_active=true/false URL filtering
        is_active = self.request.query_params.get("is_active")
        if is_active:
            # If is_active is 'true', look for records where actual_return_date IS NULL
            # If is_active is 'false', look for records where actual_return_date IS NOT NULL
            is_active_bool = is_active.lower() == "true"
            queryset = queryset.filter(actual_return_date__isnull=is_active_bool)

        return queryset

    def get_serializer_class(self):
        if self.action == "create":
            return BorrowingCreateSerializer
        else:
            return BorrowingReadSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
