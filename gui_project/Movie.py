class Movie:
    def __init__(self, idx, title, year, stars):
        self.idx = idx
        self.title = title
        self.year = year
        self.stars = stars
        
    def set_idx(self, idx):
        self.idx = idx

    def set_title(self, title):
        self.title = title

    def set_year(self, year):
        self.year = year

    def set_stars(self, stars):
        self.stars = stars

    def get_title(self, idx):
        return self.idx

    def get_title(self, title):
        return self.title

    def get_year(self, year):
        return self.year

    def get_stars(self, stars):
        return self.stars

    def __repr__(self):
        return f"Movie('Index:{self.idx}', 'Title:{self.title}', 'Year:{self.year}', 'Stars:{self.stars}')"