from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import models
from django import forms
import datetime

from .forms import UserForm, UserProfileInfoForm, UppForm, UserMatchForm, UserMatchFormOpponent
from .models import User, UserProfileInfo

# The home page.
def index(request):
    """ A view to return the index page """
    all_objects = UserProfileInfo.objects.order_by('-ratingf') # Sort by The player total rating (ratingf = total rating points)

    played_matches = 0
    for user in all_objects:
        if str(request.user) == str(user):
            played_matches = user.rating
    
    
        

    return render(request, 'home/index.html', {'all_objects': all_objects, 'played_matches': played_matches})


def wrong_404(request, exception):
    return render(request, 'home/404.html')

# The All league page whit all registrated players
def league_all(request):
     all_objects = UserProfileInfo.objects.order_by('-ratingf')
     return render(request, 'home/league_all.html', {'all_objects':all_objects})

# The Club league page whit all registrated players who registered the same club
def league_club(request):
    all_objects = UserProfileInfo.objects.order_by('-ratingf')

    for user in all_objects:
        if str(request.user) == str(user):
            club = user.club_location

    return render(request, 'home/league_club.html', {'all_objects':all_objects, 'club': club})

# The registration page where you can register matches that you have played
@login_required
def reg_match(request):
    user = request.user
    all_objects = UserProfileInfo.objects.order_by('-ratingf') # ratingf is your total rating score

    #-------------------------------------------------------
    # Gets a variable so I can remove the info button on the page after two registered matches.
    played_matches = 0
    for user in all_objects:
        if str(request.user) == str(user):
            played_matches = user.rating
    #-------------------------------------------------------

    profile = UserProfileInfo.objects.all()
    profile_len = len(profile)
    now = datetime.datetime.now()
    date = now.date() 
    rf_sum = 0.0
    turn_one = 0

    # function to check a player's highest ranking (only top 5 checked)
    # to give them an extra "variable" that is saved in DB
    for object_x in all_objects:
        if turn_one == 0:
            one = object_x.user   
            rating_one = object_x.ratingf 
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)  
            match.matcher = 'Top plac 1:a'
            match.save()

        elif turn_one == 1:
            two = object_x.user
            rating_two = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)         
            match.matcher = 'Top plac 2:a'
            if object_x.matcher != 'Top plac 1:a':
                match.save()

        elif turn_one == 2:
            three = object_x.user
            rating_three = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)         
            match.matcher = 'Top plac 3:a'
            if object_x.matcher != 'Top plac 1:a' and object_x.matcher != 'Top plac 2:a':
                match.save()

        elif turn_one == 3:
            four = object_x.user
            rating_four = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)         
            match.matcher = 'Top plac 4:a'
            if object_x.matcher != 'Top plac 1:a' and object_x.matcher != 'Top plac 2:a' and object_x.matcher != 'Top plac 3:a':
                match.save()

        elif turn_one == 4:
            five = object_x.user
            rating_five = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)         
            match.matcher = 'Top plac 5:a'
            if object_x.matcher != 'Top plac 1:a' and object_x.matcher != 'Top plac 2:a' and object_x.matcher != 'Top plac 3:a' and object_x.matcher != 'Top plac 4:a':
                match.save()

        rf_sum = rf_sum + object_x.ratingf
        if object_x.user == request.user:


            #if user.email == '' and object_x.rating > 3 and object_x.antal_vunna > 1:
                #return HttpResponseRedirect('/password_reset_uppmaning/')

            # flag is a game flag (boolean) for check if a player is activated for match play
            # flag sets to true 
            id_x = object_x.id
            flag = UserProfileInfo.objects.get(id=id_x)         
            flag.game_flag = True
            flag.save()

    return render(request, 'home/reg_match.html',{'all_objects':all_objects,
                                                        'played_matches':played_matches,
                                                        'profile':profile,
                                                         'rf_sum':rf_sum,
                                                         'one':one,
                                                         'two':two,
                                                         'three':three,
                                                         'four':four,
                                                         'five':five,
                                                         'rating_one':rating_one,
                                                         'rating_two':rating_two,
                                                         'rating_three':rating_three,
                                                         'rating_four':rating_four,
                                                         'rating_five':rating_five})

# Function that makes all checks when a user tries to register a played match.
@login_required
def edit(request):
    user = request.user

    # Check if the user is trying to score points for himself
    searchWord = request.POST.get('search')
    if searchWord == user.username:
        return HttpResponse("<br><br><h2><center><font color="'#d30f0f'"><h1> Ööööö!!!</h1> </font>Are you trying to score points for yourself ?! Big no no!<br><br> <a href=https://8000-lime-cod-wnrz8yeu.ws-eu16.gitpod.io/reg_match/> → Back ← </a></h2>")

    # Check if the input is empty
    if searchWord == '':
        return HttpResponseRedirect('/reg_match/')
    user_profile_info = UserProfileInfo.objects.all()

    for object_x in user_profile_info:

        if str(searchWord) == str(object_x.user) and user != object_x.user and user == request.user:
            print('if str(searchWord) == str(object_x.user) and user != object_x.user and user == request.user:2')
            i_opponent = object_x.id
            opponent = UserProfileInfo.objects.get(id=i_opponent)
         
            for object_xx in user_profile_info:

                if user == object_xx.user and str(searchWord) != str(user):
                    i_profile = object_xx.id
                    profile = UserProfileInfo.objects.get(id=i_profile)

                if user == object_xx.user:
                    print('if user == object_xx.user:4')
                    i_opponent = object_xx.id
 

                    opp_snitt = object_x.snitt # HÄR ÄR DB VAREABELN
                    pro_snitt = object_xx.snitt # HÄR ÄR DB VAREABELN

      
                    
                    snitt_pro = profile.snitt
                    snitt_opp = opponent.snitt

                    # Here, the rating points are calculated for the match played and saved in DB
                    if object_xx.game_flag == True:
                        all_objects = UserProfileInfo.objects.order_by('-ratingf')
                        for object_x in all_objects:
                            if object_x.user == request.user and profile.game_flag == True:
                                id_x = object_x.id
                                flag = UserProfileInfo.objects.get(id=id_x)         
                                game_flag = object_x.game_flag
                                flag.game_flag = False
                                sum_pro = profile.ratingf * 0.01

                                if profile.rating == 0 and opponent.rating == 0:
                                    print('done')
                                    snitt_pro = (profile.ratingf - 101) / (profile.rating  + 1 )
                                    snitt_opp = (opponent.ratingf - 99) / (opponent.rating + 1) 
                                    opponent.save()
                                    profile.save()

                                elif profile.rating == 0:
                                    print(' om jag är 0→ ', profile.user)
                                    snitt_pro = (profile.ratingf - 101) / (profile.rating + 1)
                                    snitt_opp = (opponent.ratingf - 100) / opponent.rating
                                    profile.save()
                                    opponent.save()
                                    
                                elif opponent.rating == 0:
                                    print(' om den andra är 0→ ', profile.user)
                                    snitt_opp = (opponent.ratingf - 99) / (opponent.rating + 1)
                                    snitt_pro = (profile.ratingf - 100) / profile.rating
                                    opponent.save()
                                    profile.save()
                                    pass
                                else:
                                    print(' om ingen är 0→ ', profile.user, ' ⤄ ', opponent.user)
                                    snitt_pro = (profile.ratingf - 100) / profile.rating 
                                    snitt_opp = (opponent.ratingf - 100) / opponent.rating
                                    opponent.save()
                                    profile.save()
                                    pass
                                
                                
                                opponent.snitt = snitt_opp
                                profile.snitt = snitt_pro

                                opponent.ratingf = opponent.ratingf + sum_pro
                                profile.ratingf = profile.ratingf - sum_pro

                                opponent.rating = opponent.rating +1 # Games played
                                profile.rating = profile.rating +1 # Games played

                                opponent.antal_vunna = opponent.antal_vunna + 1

                                now = datetime.datetime.now()
                                date = now.date()
                                # The players leatest match
                                opponent.match_uppdate = ' Won Against: ' + str(profile) + ' ￪ ' + str(date) + ' 🤩 '
                                profile.match_uppdate = ' Lost Against: ' + str(opponent) + ' ￬ ' + str(date) + ' 😡 ' 
                                flag.save()
                                opponent.save()
                                profile.save()
                                # call the game flag function
                                change_game_flag(game_flag, request)
                                
                    all_objects = UserProfileInfo.objects.order_by('-ratingf')
                    user_match_form = UserMatchForm(instance=user)
                    user_match_form_opponent = UserMatchFormOpponent()

                    #searchWord = ''
                    sum_pro = profile.ratingf * 0.01
                    return render(request,'home/edit.html',
                          {'user_match_form':user_match_form,
                          'user_match_form_opponent':user_match_form_opponent,
                          'searchWord':searchWord,
                          'all_objects':all_objects,
                          'sum_pro':sum_pro,
                          'user':user,
                          'snitt_pro':snitt_pro,
                          'snitt_opp':snitt_opp})
                    
    if request.method == 'POST':
        return HttpResponseRedirect('/reg_match/')

# The profile update page
@login_required
def update(request):
    user = request.user
    profile = UserProfileInfo.objects.get(user=request.user)
    registered = False
    reg = False

    if request.method == 'POST':
        user_form = UppForm(data=request.POST, instance=user )
        profile_form = UserProfileInfoForm(request.POST, instance=profile)

        # Check to see both forms from forms.py are valid
        if user_form.is_valid() and profile_form.is_valid():
           
            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
            user_profile_info = UserProfileInfo.objects.all()
            for object_x in user_profile_info:
                if object_x.user == request.user:
                    id_x = object_x.id

            profile = profile_form.save(commit=False)
            profile = UserProfileInfo.objects.get(id=id_x)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            profile.club_location = request.POST['club_location']
            
            # Now save model
            profile.save()
            
            # Registration Successful!
            registered = True
            reg = True
            
        #else:
            # One of the forms was invalid if this else gets called.
        #    print('>> ERROR: ',user_form.errors, profile_form.errors)

    else:

        # Was not an HTTP post so we just render the forms as blank.
        user_form = UppForm(instance=user)
        profile_form = UserProfileInfoForm(instance=profile)
        upp_form = user_form

    # This is the render and context dictionary to feed
    # back to the uppdate.html file page.
    return render(request,'home/update.html',
                          {'upp_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'reg':reg})

# The profile page where you can see your profile and update
@login_required
def profile(request):
    user = request.user
    all_objects = UserProfileInfo.objects.order_by('-ratingf')
    profile = UserProfileInfo.objects.all()
    profile_len = len(profile)
     
    now = datetime.datetime.now()
    date = now.date() 
    rf_sum = 0.0
    turn_one = 0
    
    return render(request, 'home/profile.html',{'all_objects':all_objects,
                                                        'profile':profile,
                                                         })
# Function for set the game flag for a user
def change_game_flag(game_flag, request):
    
    user= request.user
    user_profile_info = UserProfileInfo.objects.all()
    # If we have a user
    if user:
        #Check it the account is active
        if user.is_active:
            for object_x in user_profile_info:
                if object_x.user == request.user:
                    id_x = object_x.id
                    user_profile_info = object_x.user
                    f = object_x.game_flag
                    
            flag = UserProfileInfo.objects.get(id=id_x)         
            if flag.game_flag == True:
                flag.game_flag = False
            else:
                flag.game_flag = True
            flag.save()
    return game_flag
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message =  'Couronne will get back to you soon. Your Message: ' + message
            try:
                send_mail(subject, message, from_email, ['couronne@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            successView(from_email, subject, message)
            return redirect('/succes_contact_us')
    
    return render(request, 'home/contact_us.html', {'form': form})


# The couronne info page
def couronne_info(request):

    return render(request, 'home/couronne_info.html')

# Resive email success
def succes_contact_us(request):
    return render(request, 'home/succes_contact_us.html')

# when user contact us we get a mail
def successView(from_email, subject, message):
    sender = from_email
    from_email = 'svante.magnell@gmail.com'

    send_mail( subject, message, from_email,  [sender])
    

def user_login(request):
    return HttpResponseRedirect('/accounts/login')

# Registration page that overwrites the original registration (all auth)
# page for the connection between the DB tables to work.
def register(request):
    registered = False

    # Check if user is logged in. If the user is logged in, 
    # they will be forwarded to update the profile page
    profile = UserProfileInfo.objects.all()
    user = request.user

    

    for user_profile_info in profile:
        if str(user_profile_info) == str(user):
            print(user_profile_info)

            return HttpResponseRedirect('/update/')

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            user.first_name = user_form.cleaned_data['username']
            
            # Hash the password
            user.set_password(user.password)  

            # Update with Hashed password
            user.save()

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            

            #### Check if they provided a profile picture
            ###if 'profile_pic' in request.FILES:
            ###    print('>> found it')
            ###    # If yes, then grab it from the POST form reply
            ###    profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            
            profile.save()
            
            # Registration Successful!
            registered = True
            
        #else:
        #    # One of the forms was invalid if this else gets called.
        #    print('>> ERROR: ',user_form.errors, profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'home/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

