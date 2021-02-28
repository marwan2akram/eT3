from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import LeaveRequest
from leave_request.users.models import User, Profile
import datetime
from dateutil import parser
from django.forms import ValidationError


# Create your views here.

# The home page
def index(request):
    return render(request, 'users/home.html')


# A user can create his profile
def create_profile(request):
    try:
        if request.method == 'POST':
            user = request.user
            photo = request.FILES["pro-pic"]
            department = request.POST.get('department')
            manager = request.POST.get('manager')
            leave_balances = request.POST.get('leave_balances')
            if manager:
                profile = Profile(
                    user=user,
                    photo=photo,
                    department=department,
                    # Set manager to TRUE
                    manager=True,
                    leave_balances=leave_balances
                )
                profile.save()
                return redirect("leaverequests:index")
            profile = Profile(
                user=user,
                photo=photo,
                department=department,
                # Set manager to FALSE
                manager=False,
                leave_balances=leave_balances
            )
            profile.save()
            # Redirect the user to his home page after creating his profile
            return redirect("leaverequests:index")
        return render(request, 'users/add-profile.html')
    except:
        return redirect("leaverequests:index")


# A employee can create his leave request
def create_request(request):
    # only users with profile can create leave requests
    try:
        employee = request.user.profile
        # Managers can not create leave-requests
        if not employee.manager:
            if request.method == 'POST':
                error_messages = []
                # The employee cannot make a leave request if he does not have
                # sufficient leave requests balance
                if employee.leave_balances > 0:
                    date = request.POST.get('date')
                    parse_date = parser.parse(date)
                    # It is not possible to make a leave request with a past date
                    if parse_date < datetime.datetime.today():
                        error_messages.append("The date cannot be in the past!")
                        return render(request, 'users/create-request.html', {"error_messages": error_messages})
                    note = request.POST.get('note')
                    reason = request.POST.get('reason')
                    leave_request = LeaveRequest(
                        employee=employee,
                        date=date,
                        note=note,
                        reason=reason,
                    )
                    leave_request.save()
                    # The leave is deducted from the employee's balance
                    # until the manager accepts it or rejects it.
                    employee.leave_balances -= 1
                    employee.save()
                    return redirect("leaverequests:index")
                error_messages.append(" you don't have enough leave balance ")
                return render(request, 'users/create-request.html', {"error_messages": error_messages})
            return render(request, 'users/create-request.html')
        return redirect("leaverequests:index")
    except:
        return redirect("leaverequests:index")


# Return all the leave requests for the employee
def history_log(request):
    employee = request.user.profile
    approved_requests = LeaveRequest.objects.filter(employee=employee).filter(approved='Approved')
    rejected_requests = LeaveRequest.objects.filter(employee=employee).filter(approved='Rejected')
    pending_requests = LeaveRequest.objects.filter(employee=employee).filter(approved='pending')
    context = {
        "approved_requests": approved_requests,
        "rejected_requests": rejected_requests,
        "pending_requests": pending_requests
    }
    return render(request, 'users/history-log.html', context)


# Return all the leave requests to manger to be reviewed.
def history_admin_log(request):
    # only mangers can access this view
    if request.user.profile.manager:
        approved_requests = LeaveRequest.objects.all().filter(approved='Approved')
        rejected_requests = LeaveRequest.objects.all().filter(approved='Rejected')
        pending_requests = LeaveRequest.objects.all().filter(approved='pending')
        context = {
            "approved_requests": approved_requests,
            "rejected_requests": rejected_requests,
            "pending_requests": pending_requests
        }

        return render(request, 'users/history-admin-log.html', context)
    return redirect("leaverequests:index")


# Manager can approve requests.
def approve_request(request,id):
    leave_request = get_object_or_404(LeaveRequest, id=id)
    # Set the status of the request to approved
    leave_request.approved = 'Approved'
    leave_request.save()
    return redirect("leaverequests:history-admin-log")


# Manger can Reject leave requests.
def reject_request(request,id):
    leave_request = get_object_or_404(LeaveRequest, id=id)
    # Set the status of the request to Rejected
    leave_request.approved = 'Rejected'
    leave_request.save()
    employee = leave_request.employee
    # if the request is Rejected then the leave request
    # will not be deducted from the leave requests balance
    employee.leave_balances += 1
    employee.save()
    leave_request.save()
    return redirect("leaverequests:history-admin-log")
