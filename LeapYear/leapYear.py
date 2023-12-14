#leap year problem

def isLeapYear(year):
    if year % 4 == 0:           #return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

if __name__ == "__main__":
    year = 2100
    print(isLeapYear(year))