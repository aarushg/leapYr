def is_leap(year):
    leap = False

    while year % 4 == 0:

        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    return leap

def include_month_year(sm):

        if sm >= 3:
            return False

        else:
            return True

def include_day_year(sm, sd)


        if starting month is greater then 3 then we should not include the month

            if strating month is less then 3 then we should include the month

     # extending February to 29 days rather than 28

        if starting month is 2 then the day should be less then 29 to include








leap_year=()
for cy in range(cy,ey,1):

    if is_leap(cy):
        leap_year.extend(cy)




print leap_year

def main():
    print "Input a starting day(1-31)?"
    if input in range(1, 31):
        sd = int(input())

    print "Input a starting month(1-12)?"
    if input in range(1, 12):
        sm = int(input())

    print "Input a starting year?"
    sy = int(input())

    ##################################################################

    print "Input a ending day(1-31)?"
    if input in range(1, 31):
        ed = int(input())

    print "Input a ending month(1-12)?"
    if input in range(1, 12):
        em = int(input())

    print "Input a ending year?"
    ey = int(input())

main()