from django.shortcuts import render, redirect

# Create your views here.
from exam_prep_1.game_app.forms import CreatePersonForm, CreateGameForm, DeleteGameForm, DeletePersonForm, \
    EditPersonForm
from exam_prep_1.game_app.models import Person, Game
from exam_prep_1.game_app.utils import get_person, get_games, get_game_from_db, get_average_rating_for_games

"""
• http://localhost:8000/ - home page
• http://localhost:8000/profile/create - create profile page
• http://localhost:8000/dashboard/ - dashboard page
• http://localhost:8000/game/create/ - create game page
• http://localhost:8000/game/details/<id>/ - details game page
• http://localhost:8000/game/edit/<id>/ - edit game page
• http://localhost:8000/game/delete/<id>/ - delete game page
• http://localhost:8000/profile/details/ - details profile page
• http://localhost:8000/profile/edit/ - edit profile page
• http://localhost:8000/profile/delete/ - delete profile page


"""


def index(request):
    context = {
        'is_user_created': get_person(),
    }

    return render(request, 'core/home-page.html', context)


def dashboard(request):
    games = get_games()

    context = {
        'games': games,
        'is_user_created': get_person(),

    }
    return render(request, 'core/dashboard.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = CreatePersonForm()
    else:
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }

    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_person()
    games = Game.objects.all()
    average_rating = get_average_rating_for_games(games)
    game_count = len(games)

    context = {
        'is_user_created': get_person(),
        'profile': profile,
        'average_rating': average_rating,
        'game_count': game_count,
    }

    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_person()
    if request.method == 'GET':
        form = EditPersonForm(instance=profile)
    else:
        form = EditPersonForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_person()

    if request.method == 'GET':
        form = DeletePersonForm(instance=profile)
    else:
        form = DeletePersonForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'profile/delete-profile.html',
        context,
    )


def game_create(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'is_user_created': get_person(),
        'form': form

    }

    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    game = Game.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'is_user_created': get_person(),
        'game': game,
    }
    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    game = get_game_from_db(pk)

    if request.method == 'GET':
        form = CreateGameForm(instance=game)
    else:
        form = CreateGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'is_user_created': get_person(),
    }

    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    game = get_game_from_db(pk)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
        'is_user_created': get_person(),
    }

    return render(request, 'game/delete-game.html', context)
