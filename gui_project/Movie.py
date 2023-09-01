class Movie:
    def __init__(self, title, year, stars):
        self.title = title
        self.year = year
        self.stars = stars

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_stars(self, stars):
        self.stars = stars

    def get_title(self, title):
        return self.title

    def get_year(self, year):
        return self.year

    def get_stars(self, stars):
        return self.stars

    def __repr__(self):
        return f"Movie('Title:{self.title}', 'Year:{self.year}', 'Stars:{self.stars}' )"