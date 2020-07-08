from django.shortcuts import render

from .forms import SignUpForm

def signUp(request):
    if request.method=='POST':
        new_user_form = SignUpForm(request.POST)
        
        if new_user_form.is_valid():
            new_user = new_user_form.save(commit=False)
            new_user.set_password(new_user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/sign_up_complete.html', {'new_user':new_user})
    
    else:
        new_user_form = SignUpForm()

    return render(request, 'accounts/sign_up.html', {'form':new_user_form})