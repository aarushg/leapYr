import datetime
#
# def include_month_year(sm):
#
#         if sm >= 3:
#             return False
#
#         else:
#             return True
#
#         #if starting month is greater then 3 then we should not include the month
#
#          # if starting month is less then 3 then we should include the month
#
# def include_day_year(sm, sd)
#
#     if sm == 2:
#
#         if sd <=29:
#             return true
#
#
#
#
#
#      # extending February to 29 days rather than 28
#
#         if starting month is 2 then the day should be less then 29 to include
#
#
#
#
#
#
#
#
# leap_year=()
# for cy in range(cy,ey,1):
#
#     if is_leap(cy):
#         leap_year.extend(cy)
#
#
#
#
# print leap_year

def main():

    def inputdate(prompt):

        d = int(raw_input('Enter ' + prompt + ' day(1-31): '))
        while(d not in range(1,32)):
            d = int(raw_input('Enter ' + prompt + ' day(1-31): '))

        m = int(raw_input('Input a ' + prompt + ' month(1-12)?: '))
        while (m not in range(1, 13)):
            m = int(raw_input('Input a ' + prompt + ' month(1-12)?: '))

        y = int(raw_input('Enter ' + prompt + ' year: '))

        return y, m, d

    startnum = inputdate('starting')

    endnum = inputdate('ending')

    startdate = datetime.date(*startnum)
    enddate = datetime.date(*endnum)

    if not startdate<=datetime.date(startdate.year,2,28):
        startdate = datetime.date(startdate.year+1,startdate.month,startdate.day)

    if not enddate>=datetime.date(enddate.year,2,28):
        enddate = datetime.date(enddate.year-1,enddate.month,enddate.day)

    sy = startdate.year
    ey = enddate.year


    print 'Leap years between', sy, 'and', ey, 'inclusive'
    while sy <= ey:
        if sy % 4 == 0 and sy % 100 != 0:
            print sy
        if sy % 100 == 0 and sy % 400 == 0:
            print sy
        sy = sy + 1


main()
