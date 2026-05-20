from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "status",
            "type",
            "borrowings",
            "session_url",
            "session_id",
            "money_to_pay"
        )
        extra_kwargs = {
            "session_url": {"read_only": True},
            "session_id": {"read_only": True},
            "money_to_pay": {"read_only": True}
        }
