class Movie:
    def __init__(self, movie_id, movie_title, movie_year):
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.movie_year = movie_year

    def serialize(self, serializer):
        serializer.start_object('movie', self.movie_id)
        serializer.add_property('title', self.movie_title)
        serializer.add_property('year', self.movie_year)


class Performance:
    def __init__(self, performance_id, performance_title, performance_theatre):
        self.performance_id = performance_id
        self.performance_title = performance_title
        self.performance_theatre = performance_theatre

    def serialize(self, serializer):
        serializer.start_object('performance', self.performance_id)
        serializer.add_property('title', self.performance_title)
        serializer.add_property('theatre', self.performance_theatre)
