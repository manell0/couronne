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

from .forms import UserForm, UserProfileInfoForm, UppForm, UserMatchForm, \
    UserMatchFormOpponent
from .models import User, UserProfileInfo


# The home page.
def index(request):
    """ A view to return the index page """

    # Sort by The player total rating (ratingf = total rating points)
    all_objects = UserProfileInfo.objects.order_by('-ratingf')

    played_matches = 0
    for user in all_objects:
        if str(request.user) == str(user):
            played_matches = user.number_played_matches
    return render(request, 'home/index.html', {
        'all_objects': all_objects,
        'played_matches': played_matches})


def rules_story(request):
    return render(request, 'home/rules_story.html')


def wrong_404(request, exception):
    return render(request, 'home/404.html')


# The All league page whit all registrated players listed
# whit the highest ratingf on top
def league_all(request):
    all_objects = UserProfileInfo.objects.order_by('-ratingf')
    return render(request, 'home/league_all.html', {
        'all_objects': all_objects})


# Club league page whit all registrated players who registered the same club
@login_required
def league_club(request):
    all_objects = UserProfileInfo.objects.order_by('-ratingf')

    # Set club varable to avoid error message
    # (local variable 'club' referenced before assignment)
    # when try to access with admin or another user who is not in the league
    club = ' is not in the league and has no club affiliation!'

    for user in all_objects:
        if str(request.user) == str(user):
            club = user.club_location

    return render(request, 'home/league_club.html', {
        'all_objects': all_objects,
        'club': club})


# The registration page where you can register matches that you have played
@login_required
def reg_match(request):
    user = request.user

    # ratingf is your total rating score
    all_objects = UserProfileInfo.objects.order_by('-ratingf')

    # all_name = UserProfileInfo.objects.order_by('club_location')

    played_matches = 0
    for user in all_objects:
        if str(request.user) == str(user):
            played_matches = user.number_played_matches

    profile = UserProfileInfo.objects.all()
    rf_sum = 0.0
    turn_one = 0

    # function to check a player's highest ranking (only top 5 checked)
    # to give them an extra "variable" that is saved in DB and
    # appears as Best Ranking in All Players template
    for object_x in all_objects:
        if turn_one == 0:
            one = object_x.user
            rating_one = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)
            match.best_ranking = '1'
            match.save()

        elif turn_one == 1:
            two = object_x.user
            rating_two = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)
            match.best_ranking = '2'
            if object_x.best_ranking != '1':
                match.save()

        elif turn_one == 2:
            three = object_x.user
            rating_three = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)
            match.best_ranking = '3'
            if object_x.best_ranking != '1' and object_x.best_ranking != '2':
                match.save()

        elif turn_one == 3:
            four = object_x.user
            rating_four = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)
            match.best_ranking = '4'
            if object_x.best_ranking != '1' and object_x.best_ranking != '2' \
                    and object_x.best_ranking != '3':
                match.save()

        elif turn_one == 4:
            five = object_x.user
            rating_five = object_x.ratingf
            turn_one = turn_one + 1
            id_x = object_x.id
            match = UserProfileInfo.objects.get(id=id_x)
            match.best_ranking = '5'
            if object_x.best_ranking != '1' and object_x.best_ranking != '2' and \
                    object_x.best_ranking != '3' and object_x.best_ranking != '4':
                match.save()

        rf_sum = rf_sum + object_x.ratingf
        if object_x.user == request.user:

            # flag is a game flag (boolean) for check
            # if a player is activated for match play
            # flag sets to true
            id_x = object_x.id
            flag = UserProfileInfo.objects.get(id=id_x)
            flag.game_flag = True
            flag.save()

    return render(request, 'home/reg_match.html', {
        'all_objects': all_objects,
        'played_matches': played_matches,
        'profile': profile,
        'rf_sum': rf_sum,
        'one': one,
        'two': two,
        'three': three,
        'four': four,
        'five': five,
        'rating_one': rating_one,
        'rating_two': rating_two,
        'rating_three': rating_three,
        'rating_four': rating_four,
        'rating_five': rating_five})


@login_required
def reg_match_wrong(request, message, heading, final_text):
    return render(request, 'home/reg_match_wrong.html', {
        'message': message,
        'heading': heading,
        'final_text': final_text})


# Function that makes all checks when a user tries to register a played match.
@login_required
def edit(request):
    user = request.user
    user_profile_info = UserProfileInfo.objects.all()

    # Check if the user is trying to score points for himself
    searchWord = request.POST.get('search')
    if searchWord == user.username:
        heading = 'Big no no!'
        message = 'You are trying to score points for yourself!'
        final_text = "You're not a cheater, are you?"
        return render(request, 'home/reg_match_wrong.html', {
            'message': message,
            'heading': heading,
            'final_text': final_text})

    # Check if the input is empty and not admin
    if searchWord == '' or searchWord == 'admin':
        if searchWord == '':
            heading = 'Write something!'
            message = 'Enter a name to register a match.'
            final_text = 'The input is case sensitive'
        else:
            heading = 'admin is not in the league!'
            message = 'At the bottom of the page you can see names that are possible to register.'
            final_text = 'The input is case sensitive'

        return render(request, 'home/reg_match_wrong.html', {
            'message': message,
            'heading': heading,
            'final_text': final_text})

    # Check input field for misspelling
    i = 1
    for search_user in user_profile_info:
        if searchWord == str(search_user.user):
            break

        elif searchWord != search_user.user and i == len(user_profile_info):
            heading = 'Check the spelling!'
            message = 'Opponent does not exist, or you have misspelled.'
            final_text = 'The input is case sensitive'

            return render(request, 'home/reg_match_wrong.html', {
                'message': message,
                'heading': heading,
                'final_text': final_text})

        i = i + 1

    for object_x in user_profile_info:

        if str(searchWord) == str(object_x.user) and user != object_x.user \
                and user == request.user:

            i_opponent = object_x.id
            opponent = UserProfileInfo.objects.get(id=i_opponent)

            for object_xx in user_profile_info:

                if user == object_xx.user and str(searchWord) != str(user):
                    i_profile = object_xx.id
                    profile = UserProfileInfo.objects.get(id=i_profile)

                if user == object_xx.user:
                    i_opponent = object_xx.id

                    average_profile = profile.average
                    average_profile = opponent.average

                    # Here, the rating points are calculated for
                    # the match played and saved in DB
                    if object_xx.game_flag == True:
                        all_objects = UserProfileInfo.objects.order_by('-ratingf')
                        for object_x in all_objects:
                            if object_x.user == request.user and profile.game_flag == True:
                                id_x = object_x.id
                                flag = UserProfileInfo.objects.get(id=id_x)
                                game_flag = object_x.game_flag
                                flag.game_flag = False
                                sum_pro = profile.ratingf * 0.01

                                if profile.number_played_matches == 0 and opponent.number_played_matches == 0:
                                    average_profile = (profile.ratingf - 101) / (profile.number_played_matches + 1)
                                    average_profile = (opponent.ratingf - 99) / (opponent.number_played_matches + 1)
                                    opponent.save()
                                    profile.save()

                                elif profile.number_played_matches == 0:
                                    average_profile = (profile.ratingf - 101) / (profile.number_played_matches + 1)
                                    average_profile = (opponent.ratingf - 100) / opponent.number_played_matches
                                    profile.save()
                                    opponent.save()

                                elif opponent.number_played_matches == 0:
                                    average_profile = (opponent.ratingf - 99) / (opponent.number_played_matches + 1)
                                    average_profile = (profile.ratingf - 100) / profile.number_played_matches
                                    opponent.save()
                                    profile.save()

                                else:
                                    average_profile = (profile.ratingf - 100) / profile.number_played_matches
                                    average_profile = (opponent.ratingf - 100) / opponent.number_played_matches
                                    opponent.save()
                                    profile.save()

                                opponent.average = average_profile
                                profile.average = average_profile

                                opponent.ratingf = opponent.ratingf + sum_pro
                                profile.ratingf = profile.ratingf - sum_pro

                                opponent.number_played_matches = opponent.number_played_matches + 1  # Games played
                                profile.number_played_matches = profile.number_played_matches + 1  # Games played

                                opponent.matches_won = opponent.matches_won + 1

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

                    sum_pro = profile.ratingf * 0.01
                    return render(request, 'home/edit.html', {
                        'user_match_form': user_match_form,
                        'user_match_form_opponent': user_match_form_opponent,
                        'searchWord': searchWord,
                        'all_objects': all_objects,
                        'sum_pro': sum_pro,
                        'user': user,
                        'average_profile': average_profile})

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
        user_form = UppForm(data=request.POST, instance=user)
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

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UppForm(instance=user)
        profile_form = UserProfileInfoForm(instance=profile)
        # upp_form = user_form

    # This is the render and context dictionary to feed
    # back to the uppdate.html file page.
    return render(request, 'home/update.html', {
        'upp_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
        'reg': reg})


# The profile page where you can see your profile and update
@login_required
def profile(request):
    all_objects = UserProfileInfo.objects.order_by('-ratingf')
    profile = UserProfileInfo.objects.all()

    return render(request, 'home/profile.html', {
        'all_objects': all_objects,
        'profile': profile})


# Function for set the game flag for a user
def change_game_flag(game_flag, request):
    user= request.user
    user_profile_info = UserProfileInfo.objects.all()
    # If we have a user
    if user:
        #Check if the account is active
        if user.is_active:
            for object_x in user_profile_info:
                if object_x.user == request.user:
                    id_x = object_x.id
                    user_profile_info = object_x.user

            flag = UserProfileInfo.objects.get(id=id_x)
            if flag.game_flag == True:
                flag.game_flag = False
            else:
                flag.game_flag = True
            flag.save()
    return game_flag


# Contact page where user can send mail to couronne
def contact_us(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            message = 'Couronne will get back to you soon. Your Message: ' + message
            try:
                send_mail(subject, message, from_email, ['svante.magnell@gmail.com'])
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
# page for the connection between the DB (UserProfileInfo) tables to work.
def register(request):
    registered = False

    # Check if user is logged in. If the user is logged in,
    # they will be forwarded to update the profile page
    profile = UserProfileInfo.objects.all()
    user = request.user
    for user_profile_info in profile:
        if str(user_profile_info) == str(user):
            return HttpResponseRedirect('/update/')

    if request.method == 'POST':
        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():


            for item in user_form:
                pass
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

            # Now save model

            profile.save()

            # Registration Successful!
            registered = True

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'home/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered})
