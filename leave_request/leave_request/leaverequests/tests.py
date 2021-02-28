from django.test import TestCase
from .models import LeaveRequest
from leave_request.users.models import User, Profile
# Create your tests here.


class ProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('Marwan', 'Marwan@thebeatles.com', '123321Ma#')
        self.user2 = User.objects.create_user('Ahmed', 'ahmed@thebeatles.com', '123321Ma#')
        self.profile = Profile.objects.create(user=self.user, leave_balances=0)

    # Test profile  can be created
    def test_profile_fields(self):
        profile = Profile()
        profile.user = self.user2
        # positive leave balances
        profile.leave_balances = 29
        profile.save()
        record = Profile.objects.last()
        self.assertEqual(record, profile)

    # Test leave request  can be created
    def test_create_leave_request(self):
        leave_reaquest=LeaveRequest()
        leave_reaquest.employee = self.profile
        leave_reaquest.date = "2021-02-02"
        leave_reaquest.save()
        record = LeaveRequest.objects.get(id=1)
        self.assertEqual(record,leave_reaquest)

