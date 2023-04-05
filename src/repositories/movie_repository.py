from src.models import db, Movies


class MovieRepository:

    def get_all_movies(self):
        all = Movies.query.all()
        return all

    def get_movie_by_id(self, movie_id):
        ids = Movies.query.get(movie_id)
        return ids

    def create_movie(self, title, director, rating):
        new = Movies(title = title, director =director, rating =rating)
        db.session.add(new)
        db.session.commit()
        return new

    def search_movies(self, title):
        search = Movies.query.filterby(title).all()
        return search


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
