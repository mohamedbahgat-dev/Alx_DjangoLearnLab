from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_librarian(user):
    return bool(getattr(user, "is_authenticated", False) and
                getattr(user, "profile", None) and
                user.profile.role == 'librarian')

@user_passes_test(is_librarian, login_url='login', redirect_field_name='next')
def librarian_view(request):
    return HttpResponse("Librarian-only content")

