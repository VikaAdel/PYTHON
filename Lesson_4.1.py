num = 3
def today(day):
    if day == 0:
        return '+'
    number = input()
    return today(day-1) + number
    print(today(num))