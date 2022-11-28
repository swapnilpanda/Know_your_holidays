from calendar_info import *


def get_holiday(Year, Country):
    # Weekday Functions
    def weeknum(dayname):
        if dayname == 'Monday':   return 0
        if dayname == 'Tuesday':  return 1
        if dayname == 'Wednesday': return 2
        if dayname == 'Thursday': return 3
        if dayname == 'Friday':   return 4
        if dayname == 'Saturday': return 5
        if dayname == 'Sunday':   return 6

    from datetime import date, timedelta
    def alldays(year, whichDayYouWant):
        d = date(year, 1, 1)
        d += timedelta(days=(weeknum(whichDayYouWant) - d.weekday()) % 7)
        while d.year == year:
            yield d
            d += timedelta(days=7)

    Saturdays = []
    for d in alldays(Year, 'Saturday'):
        Saturdays.append(d)

    Fridays = []
    for d in alldays(Year, 'Friday'):
        Fridays.append(d)

    weekends = Saturdays + Fridays

    # Getting holidays from Vakanti

    holidays = Holidays()
    holidays_others = (Holidays().get_holidays(years=Year, country=Country))
    print(holidays_others)

    holidays_o = list(holidays_others.keys())

    holidays_total = holidays_o
    holidays_total = sorted(holidays_total)
    weekend_total = weekends
    weekend_total = sorted(weekend_total)

    holidays_total = set(holidays_total)
    holidays_total = list(holidays_total)
    holidays_final = sorted(holidays_total)

    weekend_total = set(weekend_total)
    weekend_total= list(weekend_total)
    weekend_final = sorted(weekend_total)

    from datetime import timedelta, date

    def daterange(date1, date2):
        for n in range(int((date2 - date1).days) + 1):
            yield date1 + timedelta(n)

    start_dt = date(Year, 1, 1)
    end_dt = date(Year, 12, 31)
    all_dates = []
    for dt in daterange(start_dt, end_dt):
        all_dates.append(dt)

    all_dates_pd = pd.to_datetime(all_dates)
    holidays_final_pd = pd.to_datetime(holidays_final)
    weekend_final_pd = pd.to_datetime(weekend_final)


    Dates = pd.DataFrame(all_dates_pd, columns=['Dates'])
    Dates['Type'] = 'Weekday'

    hol = pd.DataFrame(holidays_final_pd, columns=['Dates'])
    weekend=pd.DataFrame(weekend_final_pd, columns=['Dates'])
    for i in hol['Dates']:
        for j in range(len(Dates['Dates'])):
            if i == Dates['Dates'][j]:
                Dates['Type'][j] = 'Holiday'
    for i in weekend['Dates']:
        for j in range(len(Dates['Dates'])):
            if i == Dates['Dates'][j]:
                Dates['Type'][j] = 'Weekend'

    Dates.to_csv(f'Dates_{Year}.csv')


# get_holidays(2012, 'Bangladesh')
# get_holidays(2013, 'Bangladesh')
# get_holidays(2014, 'Bangladesh')
# get_holiday(2015, 'Bangladesh')
# get_holiday(2016, 'Bangladesh')
# get_holiday(2017, 'Bangladesh')
# get_holiday(2018, 'Bangladesh')
get_holiday(2019, 'Bangladesh')

