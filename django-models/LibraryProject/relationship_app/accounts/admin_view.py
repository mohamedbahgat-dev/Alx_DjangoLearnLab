from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_admin(user):
    return bool(getattr(user, "is_authenticated", False) and
                getattr(user, "profile", None) and
                user.profile.role == 'admin')

@user_passes_test(is_admin, login_url='login', redirect_field_name='next')
def admin_view(request):
    return HttpResponse("Admin-only content")
