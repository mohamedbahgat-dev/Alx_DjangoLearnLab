from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_member(user):
    return bool(getattr(user, "is_authenticated", False) and
                getattr(user, "profile", None) and
                user.profile.role == 'member')

@user_passes_test(is_member, login_url='login', redirect_field_name='next')
def member_view(request):
    return HttpResponse("Member-only content")
