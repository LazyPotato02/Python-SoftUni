"""
# • http://localhost:8000/ - home page
# • http://localhost:8000/profile/create - create profile page
# • http://localhost:8000/dashboard/ - dashboard page
# • http://localhost:8000/game/create/ - create game page
# • http://localhost:8000/game/details/<id>/ - details game page
# • http://localhost:8000/game/edit/<id>/ - edit game page
# • http://localhost:8000/game/delete/<id>/ - delete game page
# • http://localhost:8000/profile/details/ - details profile page
# • http://localhost:8000/profile/edit/ - edit profile page
# • http://localhost:8000/profile/delete/ - delete profile page


"""
from django.urls import path, include

from exam_prep_1.game_app.views import index, profile_create, profile_details, profile_edit, profile_delete, \
    game_create, game_details, game_edit, game_delete, dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', include([
        path('create/', profile_create, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete'),
    ])),
    path('game/', include([
        path('create/', game_create, name='game create'),
        path('details/<int:pk>/', game_details, name='game details'),
        path('edit/<int:pk>/', game_edit, name='game edit'),
        path('delete/<int:pk>/', game_delete, name='game delete'),
    ]))

]
