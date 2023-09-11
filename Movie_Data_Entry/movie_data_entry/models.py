import csv
from pathlib import Path
import os
from .constants import FieldTypes as FT
from decimal import Decimal
from datetime import datetime

class Movie:
    
    fields = {
    "Title": {'req': True, 'type': FT.string},
    "Year": {'req': True, 'type': FT.string},
    "Stars": {'req': True, 'type':  FT.string},
    }
    
    def __init__(self):
        # self.title = title
        # self.year = year
        # self.stars = stars
        
        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = "movie_data_record_{}.csv".format(datestring)
        self.file = Path(filename)

        # Check for append permissions:
        file_exists = os.access(self.file, os.F_OK)
        parent_writeable = os.access(self.file.parent, os.W_OK)
        file_writeable = os.access(self.file, os.W_OK)
        if ((not file_exists and not parent_writeable) 
            or (file_exists and not file_writeable)):
           msg = f'Permission denied accessing file: {filename}'
           raise PermissionError(msg)
     
    # def save_record(self, data):
    #     """Save a dict of data to the CSV file"""
    #     newfile = not self.file.exists()

    #     with open(self.file, 'a', newline='') as fh:
    #         csvwriter = csv.DictWriter(fh, fieldnames=self.fields.keys())
    #         if newfile:
    #          csvwriter.writeheader()

    #         csvwriter.writerow(data)        
        
        
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
        return f"Movie('Title:{self.title}', 'Year:{self.year}', 'Stars:{self.stars}')"