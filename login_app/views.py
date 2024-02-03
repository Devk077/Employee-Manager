from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def profile_page(request):
    return render(request,'profile_page.html')

def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('UserName')
        password = request.POST.get('Password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                print('login succcesfull!!')

                if 'next' in request.POST:
                    return HttpResponseRedirect(request.POST['next'])

                return HttpResponseRedirect(reverse('emp_app:index'))
            else :
                print('user not active')   
                return HttpResponseRedirect(reverse('login_app:login'))     
        else:
            print(f'worng username and password {username} and {password}')
            messages.error(request, 'Incorrect username or password. Please try again.')
            return HttpResponseRedirect(reverse('login_app:login'))
    else:
        return render(request,'login.html')

@login_required
def special(request):
    return HttpResponse("<h1>Congratulations</h1><br>This is special page and you made it here by loggin in!")


@login_required
def logoutUser(request):
    logout(request)
    print('logout succesfull')
    return HttpResponseRedirect(reverse('login_app:profile_page'))
