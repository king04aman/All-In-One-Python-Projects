from imdb import IMDb
import random


class ChooseMovie(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top250 = self.cursor.get_top250_movies()

    def __repr__(self):
        num = int(random.randint(0, 249))
        return str(f"\n\n\t{num}: {self.top250[num]}\n\n")


if __name__ == '__main__':
    print(ChooseMovie())