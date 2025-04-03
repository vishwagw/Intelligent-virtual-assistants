import datetime

def date():
    try:
        date = datetime.datetime.now().strftime("%d %b %Y")
    except Exception as e:
        print(e)
        date = False
    return date

def time():
    try:
        time = datetime.datetime.now().strftime("%H %M %S")
    except Exception as e:
        print(e)
        time = False
    return time

#return date and time as strings.

