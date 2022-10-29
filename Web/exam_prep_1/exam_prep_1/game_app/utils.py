from exam_prep_1.game_app.models import Person, Game


def get_person():
    try:
        return Person.objects.get()
    except Person.DoesNotExist:
        return None


def get_games():
    try:
        return Game.objects.all()
    except Game.DoesNotExist:
        return None


def get_game_from_db(pk):
    try:
        game = Game.objects \
            .filter(pk=pk) \
            .get()
        return game
    except Game.DoesNotExist:
        pass


def get_average_rating_for_games(games):
    try:
        games = Game.objects.all()
        average_rating = sum(game.rating for game in games) / len(games)
        return average_rating

    except ZeroDivisionError:
        average_rating = 0
        return average_rating
