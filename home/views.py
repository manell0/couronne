from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

from django.contrib import messages
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
# Create your views here.

def index(request):
    """ A view to return the index page """
    all_objects = UserProfileInfo.objects.order_by('-ratingf')
    return render(request, 'home/index.html', {'all_objects': all_objects})

@login_required
def reg_match(request):
    
    
    user = request.user
   
    

    print(' ----------------------------------------------------------------------- USER')
    all_objects = UserProfileInfo.objects.order_by('-ratingf')
    profile = UserProfileInfo.objects.all()
    rf_len = len(profile)
    print('---------------- ANTAL MEDLEMMAR! ---------------- →> ', rf_len)
       
    
     
    a = range(rf_len)
    b = sum(a)
    print('testar func sum() =',b, ' och avarabeln är: → ', a)
    nu = datetime.datetime.now()
    datum = nu.date() 
    rf_sum = 0.0
    snurr_ett = 0
    for x in all_objects:
        if snurr_ett == 0:
            ett = x.user
            rat_ett = x.ratingf
            snurr_ett = snurr_ett + 1

            i = x.id
            match = UserProfileInfo.objects.get(id=i)  
            match.matcher = 'Top plac 1:a'
            match.save()


        elif snurr_ett == 1:
            tva = x.user
            rat_tva = x.ratingf
            snurr_ett = snurr_ett + 1

            i = x.id
            match = UserProfileInfo.objects.get(id=i)         
            match.matcher = 'Top plac 2:a'
            if x.matcher != 'Top plac 1:a':
                match.save()

        elif snurr_ett == 2:
            tre = x.user
            rat_tre = x.ratingf
            snurr_ett = snurr_ett + 1

            i = x.id
            match = UserProfileInfo.objects.get(id=i)         
            match.matcher = 'Top plac 3:a'
            if x.matcher != 'Top plac 1:a' and x.matcher != 'Top plac 2:a':
                match.save()

        elif snurr_ett == 3:
            fyra = x.user
            rat_fyra = x.ratingf
            snurr_ett = snurr_ett + 1

            i = x.id
            match = UserProfileInfo.objects.get(id=i)         
            match.matcher = 'Top plac 4:a'
            if x.matcher != 'Top plac 1:a' and x.matcher != 'Top plac 2:a' and x.matcher != 'Top plac 3:a':
                match.save()

        elif snurr_ett == 4:
            fem = x.user
            rat_fem = x.ratingf
            snurr_ett = snurr_ett + 1

            i = x.id
            match = UserProfileInfo.objects.get(id=i)         
            match.matcher = 'Top plac 5:a'
            if x.matcher != 'Top plac 1:a' and x.matcher != 'Top plac 2:a' and x.matcher != 'Top plac 3:a' and x.matcher != 'Top plac 4:a':
                match.save()

        rf_sum = rf_sum + x.ratingf
        if x.user == request.user:
            
            


            if user.email == '' and x.rating > 3 and x.antal_vunna > 1:
                return HttpResponseRedirect('/password_reset_uppmaning/')

            i = x.id
            print('  user     >>>:- ', user, '↔', x.user)
            print('  id       >>>:- ', i)
            print('  rating   >>>:- ', x.rating)
            print('  flag   >>>:- ', x.game_flag)
            print('  ratingf   >>>:- ', x.ratingf)

            flag = UserProfileInfo.objects.get(id=i)         
            flag.game_flag = True
            print(' -flaggan:', flag.game_flag)
            flag.save()

    
    print('------------------------------------------------------ /USER')
    print(' ')    
    return render(request, 'home/reg_match.html',{'all_objects':all_objects,
                                                        'profile':profile,
                                                         'rf_sum':rf_sum,
                                                         'ett':ett,
                                                         'tva':tva,
                                                         'tre':tre,
                                                         'fyra':fyra,
                                                         'fem':fem,
                                                         'rat_ett':rat_ett,
                                                         'rat_tva':rat_tva,
                                                         'rat_tre':rat_tre,
                                                         'rat_fyra':rat_fyra,
                                                         'rat_fem':rat_fem})

@login_required
def edit(request):
    user = request.user
    print(user, '----------------------------------------------------------------EDIT ÖVERST')

    searchWord = request.POST.get('search')
    if searchWord == user.username:
        print('sökork---user.fist_name--------',searchWord, '--------------- sökord')
        return HttpResponse("<br><br><h2><center><font color="'#d30f0f'"><h1> Ööööö!!!</h1> </font>Försöker du ge poäng till dig själv?! Aja baja!<br><br> <a href=http://127.0.0.1:8000/home/reg_match/> → Tillbaka ← </a></h2>")

    if searchWord == '':
        print('sökork------ tomt -----',searchWord, '--------------- sökord')
        return HttpResponseRedirect('/reg_match/')
    
    p = UserProfileInfo.objects.all()
    for x in p:
        if x.user == searchWord and x.game_flag == True:
            print('if x.user == searchWord and x.game_flag == True:1')
            print('- searchWord: ' , searchWord)
            print('- x.game_flag: ' , searchWord)
            
        if str(searchWord) == str(x.user) and user != x.user and user == request.user:
            print('if str(searchWord) == str(x.user) and user != x.user and user == request.user:2')
            i_opponent = x.id
            opponent = UserProfileInfo.objects.get(id=i_opponent)
         
            for xx in p:
            #    i = xx.id
            #    xx = UserProfileInfo.objects.get(id=i)
            #    if xx.rating < 1:
            #        xx.rating = xx.rating + 1
            #        xx.save()
            #        pass



                if user == xx.user and str(searchWord) != str(user):
                    print('if user == xx.user and str(searchWord) != str(user):3')
                    i_profile = xx.id
                    profile = UserProfileInfo.objects.get(id=i_profile)

                if user == xx.user:
                    print('if user == xx.user:4')
                    i_opponent = xx.id
 

                    opp_snitt = x.snitt # HÄR ÄR DB VAREABELN
                    pro_snitt = xx.snitt # HÄR ÄR DB VAREABELN

      
                    
                    snitt_pro = profile.snitt
                    snitt_opp = opponent.snitt


                    print('---------------------------------------------innan if xx --------------------------------------')
                    if xx.game_flag == True:
                        print('-----------------------------------------efter if xx --------------------------------------')
                        
                        messages.success(request,"Matchresultatet är nu sparat och går inte att ångra!")
                    
                        all_objects = UserProfileInfo.objects.order_by('-ratingf')
                        for x in all_objects:
                            if x.user == request.user and profile.game_flag == True:
                                i = x.id
                                flag = UserProfileInfo.objects.get(id=i)         
                                game_flag = x.game_flag
                                
                                flag.game_flag = False
                                sum_pro = profile.ratingf * 0.01

                                if profile.rating == 0 and opponent.rating == 0:
                                    print('done')
                                    #break
                                    snitt_pro = (profile.ratingf - 101) / (profile.rating  + 1 )
                                    snitt_opp = (opponent.ratingf - 99) / (opponent.rating + 1) 
                                    opponent.save()
                                    profile.save()
                                    pass
                                elif profile.rating == 0:
                                    print(' om jag är 0→ ', profile.user)
                                    snitt_pro = (profile.ratingf - 101) / (profile.rating + 1)
                                    snitt_opp = (opponent.ratingf - 100) / opponent.rating
                                    profile.save()
                                    opponent.save()
                                    
                                    pass
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
#-----------------------------------------------

                                opponent.ratingf = opponent.ratingf + sum_pro
                                print(' --------------------------------------------Inte MITTEN ------------------------------------------')
                                profile.ratingf = profile.ratingf - sum_pro

                                opponent.rating = opponent.rating +1 # Spelade matcher
                                profile.rating = profile.rating +1 # Spelade matcher

                                opponent.antal_vunna = opponent.antal_vunna + 1

                                print('opponent: ', opponent, 'opponent match uppdate: ', opponent.match_uppdate)
                                print('profile: ', profile, 'user match uppdate: ', profile.match_uppdate)
                                print(datetime.time())
                                nu = datetime.datetime.now()
                                datum = nu.date()
                                print(datum, ' och så nu: ',nu)
                                opponent.match_uppdate = ' ⭐ Vinnst mot: ' + str(profile) + ' ￪ ' + str(datum) + ' ✔ '
                                profile.match_uppdate = ' 💀 Förlust mot: ' + str(opponent) + ' ￬ ' + str(datum) + ' 😡 ' 
#-------------------------------------------
                                
                                flag.save()
                                opponent.save()
                                profile.save()
                                
                                change_game_flag(game_flag, request)
                                
                                print('--flaggan:', flag, ' game_flag efter spar: ',flag.game_flag,' game_flag innan spar: ', game_flag ) 
                                print('------------------------------------------------------------------------------EDIT EFTER SPARAT')


                                #print('game_flag: ', xx.game_flag, ' xx.user', xx.user, ' user: ', user)

                    #print('→→→→→→→→→→→→→→→→ gottit tottit', 'mellanrum',i_opponent, x.game_flag, x.user, x.id, '←↔→', i_profile, 'mellanrum', xx.game_flag, xx.user, xx.id,' ←←←←←←←←←←←←←←←')
                    print(' ')
                    
                    all_objects = UserProfileInfo.objects.order_by('-ratingf')
                    user_match_form = UserMatchForm(instance=user)
                    user_match_form_opponent = UserMatchFormOpponent()

                    #searchWord = ''
                    sum_pro = profile.ratingf * 0.01
                    print('---------------------------------------------innan RENDER --------------------------------------')
                    return render(request,'home/edit.html',
                          {'user_match_form':user_match_form,
                          'user_match_form_opponent':user_match_form_opponent,
                          'searchWord':searchWord,
                          'all_objects':all_objects,
                          'sum_pro':sum_pro,
                          'user':user,
                          'snitt_pro':snitt_pro,
                          'snitt_opp':snitt_opp})
        
                    #return HttpResponseRedirect('/edit/')
                    #return HttpResponseRedirect(reverse('users'))
    print(' --------------------------------------------  -------------------------------  EDIT -------------------------------------------- efter return render' )
    print('' )

    if request.method == 'POST':
        print('------------------------------------- LÄNGST NER, HttpResponseRedirect --------------------------/EDIT HEJ DÅ')
        return HttpResponseRedirect('/reg_match/')


@login_required
def update(request):
    print(' >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> UPDATE')
    user = request.user
    profile = UserProfileInfo.objects.get(user=request.user)
    #verify = VerForm.objects.get(user=request.user)

    registered = False
    reg = False
    #password = request.user.password

    if request.method == 'POST':
        user_form = UppForm(data=request.POST, instance=user )
        profile_form = UserProfileInfoForm(request.POST, instance=profile)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            #print('>>>>>>>>>>>#####------'+ user_form.cleaned_data['user'])
           
            # Save User Form to Database
            user = user_form.save()
            print('  <<<<<<<<<<<<<>>>>>>>>>>> user: ', user)

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!
            # Can't commit yet because we still need to manipulate
    #---------------------------------------------------------------
            p = UserProfileInfo.objects.all()
            for x in p:
                if x.user == request.user:
                    i = x.id
                    print('  ratingf   >>>:- ', i)    
    #---------------------------------------------------------------
            profile = profile_form.save(commit=False)
            profile = UserProfileInfo.objects.get(id=i)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            #profile.rating = profile.rating + 10

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('>> found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

               
            profile.club_location = request.POST['club_location']
            # Now save model
           
            profile.save()
            
            # Registration Successful!
            registered = True
            reg = True
            
        else:
            # One of the forms was invalid if this else gets called.
            print('>> ERROR: ',user_form.errors, profile_form.errors)

    else:

        # Was not an HTTP post so we just render the forms as blank.
        # username = request.user
        # password = user.password
        # user = authenticate(username=username, password=password)
        
        user_form = UppForm(instance=user)
        profile_form = UserProfileInfoForm(instance=profile)
        upp_form = user_form

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'home/update.html',
                          {'upp_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered,
                           'reg':reg})


def change_game_flag(game_flag, request):
    
    user= request.user
    p = UserProfileInfo.objects.all()
    # If we have a user
    if user:
        #Check it the account is active
        if user.is_active:
            for x in p:
                if x.user == request.user:
                    i = x.id
                    p = x.user
                    f = x.game_flag
                    
            flag = UserProfileInfo.objects.get(id=i)         
            if flag.game_flag == True:
                flag.game_flag = False
            else:
                flag.game_flag = True
            flag.save()
    print(' ----->>>>>> CHANGE GAME FLAG to:', user, ' till ', flag.game_flag)
    return game_flag

def couronne_info(request):
    #return HttpResponseRedirect('couronne_info')
    #return HttpResponseRedirect('')
    
    return render(request, 'home/couronne_info.html')

def successView(request):
    return HttpResponse("<br><br><h2><center><font color="'green'"><h1> Tack för ditt meddelande</h1> Vi åtrkommer snarast<br><br> <a href=http://127.0.0.1:8000/> → Tillbaka ← </a></font></h2>")

def register(request):
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> REGISTER')
    registered = False
    
    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            print('>>>>>>>>>>>#####------'+ user_form.cleaned_data['username'])

            # Save User Form to Database
           
            user = user_form.save()

            user.first_name = user_form.cleaned_data['username']
            print('  <<<<<<<<<<<<<>>>>>>>>>>> user: ', user.first_name)
            
            # Hash the password
            user.set_password(user.password)  

            # Update with Hashed password
            user.save()
    #  ('>> user.save(): ',user.save())        

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)
            
            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user
            

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('>> found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            
            profile.save()
            
            # Registration Successful!
            registered = True
            
        else:
            # One of the forms was invalid if this else gets called.
            print('>> ERROR: ',user_form.errors, profile_form.errors)

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

def upp(request):
    """ A view to return the index page """
    all_objects = UserProfileInfo.objects.order_by('ratingf')
    return render(request, 'home/index.html', {'all_objects': all_objects})
