from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Illness, PhysicalActivities, DietPlan, DietSupplement, UserBMI

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, BMIForm

import random 

def index(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users-home')


@login_required
def profile(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def bmi(request):
    stuff = UserBMI.objects.filter(user_id=request.user.id).order_by('-date')
    p = Paginator(stuff, 7)
    page = request.GET.get('page',1)

    try:
        userRecords = p.page(page)
    except EmptyPage:
        userRecords = p.page(1)
    if request.GET.get('weight') and request.GET.get('height'):
        weight = request.GET.get('weight')
        height = request.GET.get('height')
        BMI = round(float(weight)/((float(height)/100)**2), 2)
        if BMI < 18.5:
            classification = "Underweight"
        elif BMI > 18.4 and BMI < 25.1:
            classification = "Normal"
        elif BMI > 25 and BMI < 30:
            classification = "Overweight"
        elif BMI >= 30 and BMI < 35:
            classification = "Obese"
        elif BMI >=35:
            classification = "Extremely Obese"
        #Save Data
        userBMI = UserBMI()
        userBMI.user = request.user
        userBMI.classification = classification
        userBMI.bmi = BMI
        userBMI.save()
        #Reload
        return redirect('/bmi/')
    else: 
        try: 
            userBMI = UserBMI.objects.filter(user_id=request.user.id).latest()
            request.session['classification'] = userBMI.classification
            return render(request, 'users/logged/bmi.html', {
            'bmi_form': BMIForm, 'classification': userBMI.classification, 'bmi': userBMI.bmi, 'records': userRecords,
            })
        except:
            return render(request, 'users/logged/bmi.html', {
            'bmi_form': BMIForm, 'records': userRecords, })
        
@login_required
def diet_plan(request):
    
    if request.GET.get('classification'):
        stuff = DietPlan.objects.filter(classification=request.GET.get('classification'))
        p = Paginator(stuff, 7)
        page = request.GET.get('page',1)

        try:
            page = p.page(page)
        except EmptyPage:
            page = p.page(1)

        return render(request, 'users/logged/diet_plan.html', {
            'plans': page, 'title': 'for ' + request.GET.get('classification') + ' BMI',
        })
    elif request.GET.get('category'):
        stuff = DietPlan.objects.filter(category=request.GET.get('category'))
        p = Paginator(stuff, 10)
        page = request.GET.get('page',1)

        try:
            page = p.page(page)
        except EmptyPage:
            page = p.page(1)
        return render(request, 'users/logged/diet_plan.html', {
            'plans': page
        })
    if request.GET.get('generate'):
        list1 = list(DietPlan.objects.filter(classification=request.GET.get('generate')))
        list1 = random.sample(list1, 7)
        daylist = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        for i in range(7):
            list1[i].day = daylist[i]
        return render(request, 'users/logged/diet_plan.html', {
            'plans_1': list1
        })
    else:
        try:
            stuff = DietPlan.objects.filter(classification=request.session['classification'])
        except KeyError:
            stuff = DietPlan.objects.all()
        p = Paginator(stuff, 10)
        page = request.GET.get('page',1)

        try:
            page = p.page(page)
        except EmptyPage:
            page = p.page(1)

        return render(request, 'users/logged/diet_plan.html', {'plans': page})

@login_required
def diet_supplement(request):
    if request.GET.get('classification'):
        stuff = DietSupplement.objects.filter(classification=request.GET.get('classification'))
    elif request.GET.get('category'):
        stuff = DietSupplement.objects.filter(category=request.GET.get('category'))
    else:
        try:
            stuff = DietSupplement.objects.filter(classification=request.session['classification'])
        except KeyError:
            stuff = DietSupplement.objects.all()
    p = Paginator(stuff, 10)
    page = request.GET.get('page',1)

    try:
        page = p.page(page)
    except EmptyPage:
        page = p.page(1)
    
    return render(request, 'users/logged/diet_supplement.html', {
            'supplements': page
        })
@login_required
def activities(request):
    
    if request.GET.get('classification'):
        stuff = PhysicalActivities.objects.filter(classification=request.GET.get('classification'))
    else:
        try:
            stuff = PhysicalActivities.objects.filter(classification=request.session['classification'])
        except KeyError:
            stuff = PhysicalActivities.objects.all()
    p = Paginator(stuff,10)
    page = request.GET.get('page',1)

    try:
        page = p.page(page)
    except EmptyPage:
        page = p.page(1)
    
    return render(request, 'users/logged/activities.html', {
        'activities': page
    })
    
@login_required
def common_illness(request):
    stuff = Illness.objects.all()
    p = Paginator(stuff, 10)
    page = request.GET.get('page',1)

    try:
        page = p.page(page)
    except EmptyPage:
        page = p.page(1)
    
    return render(request, 'users/logged/common_illness.html', {
        'illnesses': page
    }) 