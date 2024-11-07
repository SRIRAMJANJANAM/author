from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')


from django.contrib.auth.decorators import login_required
@login_required
def java_view(request):
    return render(request,'testapp/java.html')

@login_required
def python_view(request):
    return render(request,'testapp/python.html')

def logout_view(request):
    return render(request,'testapp/logout.html')


from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)#To hash password
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/signup.html', {'form': form})