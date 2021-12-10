from datetime import date

events = [
    "zco",
    "kvpy"
]

event_date = [
    "17/12",
    "31/12"
]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def daystogo(event, event_date):
    today = date.today()
    today_date = int(today.strftime("%d"))
    today_month = int(today.strftime("%m"))

    if (today_month == int(event_date.split('/')[1])):
        print(bcolors.WARNING, int(event_date.split('/')[0]) - today_date, " days to go for ", event, bcolors.ENDC)
    else:
        print(bcolors.WARNING, int(event_date.split('/')[0]) - today_date, " days and ", int(event_date.split('/')[1]) - today_date, " months to go for ", event, bcolors.ENDC)

for i in range(len(events)):
    daystogo(events[i], event_date[i])
