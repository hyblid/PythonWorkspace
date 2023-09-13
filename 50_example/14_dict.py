from datetime import datetime, timedelta
from datetime import date

def resturant1():
    menu = { "tea": 7, "sandwitch":10}
    total = 0
    while True:
        order = input("Order:").strip()
        if not order:
            break
        elif order in menu:
            price = menu[order]
            total += price
            print(f"{order}  costs {price}, total is {total}")
        else:
            print(f"Sorry, we are fresh out of {order} today.")

def login():
    credential = {"howard": "-5353764181694863585", "james" : "yyyy"}
    while True:
        username = input("Please enter username: ").strip()
        password = input("please enter password: ").strip()
        if not username:
            break
        elif username in credential:
            if credential[username] == password:
                print("Successful Login")
            else:
                print("Wrong password")
        else:
            print("Wrong username and password")
            
TEMPS = {'2020-08-16': 30, '2020-08-17': 32, '2020-08-18': 32, }            
def temps():
    while True:
        today = input("Enter date in YYYY-MM-DD format:").strip()

        if not today:
            break

        if len(today) != 10:
            print(f'Invalid format; try again. ')
            continue

        if today.count('-') != 2:
            print(f'Invalid format; try again. ')
            continue

        if today not in TEMPS:
            print(f'The date {today} is unknown; try again. ')
            continue

        try:
            today_date = datetime.fromisoformat(today).date()
        except ValueError as e:
            print(f'Not a valid date string; try again. ')
            continue

        yesterday_date = str(today_date - timedelta(1))
        tomorrow_date = str(today_date + timedelta(1))

        print(f'{yesterday_date}: {TEMPS.get(yesterday_date, "No data available")}')
        print(f'{today_date}: {TEMPS[str(today_date)]}')
        print(f'{tomorrow_date}: {TEMPS.get(tomorrow_date, "No data available")}')
                     
PEOPLE = {'Reuven': date.fromisoformat('1970-07-14'),
          'Atara': date.fromisoformat('2000-12-16'),
          'Shikma': date.fromisoformat('2002-12-17'),
          'Amotz': date.fromisoformat('2005-10-31')
          }             

def calculate_days():
    while True:
        name = input("Enter a person's name: ").strip()

        if not name:
            break

        today = date.today()

        if name in PEOPLE:
            print(f'{name} is {(today - PEOPLE[name]).days}')
        else:
            print(f'{name} is not in the system.')

 
    