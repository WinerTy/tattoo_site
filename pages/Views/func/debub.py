from django.shortcuts import redirect


def clear_session(request):
    request.session.flush()
    return redirect("home")
