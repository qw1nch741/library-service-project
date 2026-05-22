from django.contrib import admin
from .models import Borrowing

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "borrow_date", "expected_return_date", "actual_return_date")
    list_filter = ("expected_return_date", "actual_return_date")