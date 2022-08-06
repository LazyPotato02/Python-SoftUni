from problem_2.project.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 6):
        super().__init__(title)