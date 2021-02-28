from django.db import models
from leave_request.users.models import User, Profile
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

REASON_CHOICES = (
    ('Sick', 'Sick',),
    ('Family Reasons', 'Family Reasons',),
    ('Personal Leave', 'Personal Leave',),
    ('Leave without pay', 'Leave without pay',),
    ('Other', 'Other',),
)

APPROVAL_CHOICES = (
    ('Approved', 'Approved',),
    ('Rejected', 'Rejected',),
    ('pending', 'pending',),
)


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='leaverequest')
    date = models.DateField(null=False, blank=False, validators=[MinValueValidator(limit_value=date.today)])
    note = models.TextField(null=True, blank=True)
    reason = models.CharField(
        max_length=20,
        choices=REASON_CHOICES,
        default='Sick'
    )
    approved = models.CharField(
        max_length=20,
        choices=APPROVAL_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.employee)
