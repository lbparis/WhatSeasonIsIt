input_month = str.title((input("Enter a Month: ")))
input_month = input_month.strip()
input_day = int(input("Enter a day of the month: "))


if (input_month == 'March') and (input_day >= 20) and (input_day <= 31):
    print('It is Spring')

elif (input_month == 'April') and (0 < input_day <= 30):
    print('It is Spring')

elif (input_month == 'May') and (0 < input_day <= 31):
    print('It is Spring')

elif input_month == 'June':
    if (input_day <= 20) and (input_day > 0):
        print('It is Spring')
    elif (input_day >= 21 and input_day <= 30):
        print('It is Summer')
    else:
        print('{} {} is not a valid date.'.format(input_month, input_day))

elif (input_month == 'July') and (0 < input_day <= 31):
    print('It is Summer')

elif (input_month == 'August') and (0 < input_day <= 31):
    print('It is Summer')

elif input_month == 'September':
    if (input_day > 0) and (input_day <= 21):
        print('It is Summer')
    elif (input_day >= 22) and (input_day <= 30):
        print('It is Autumn')
    else:
        print('{} {} is not a valid date.'.format(input_month, input_day))

elif (input_month == 'October') and (0 < input_day <= 31):
    print('It is Autumn')

elif (input_month == 'November') and (0 < input_day <= 30):
    print('It is Autumn')

elif input_month == 'December':
    if (input_day <= 20) and (input_day > 0):
        print('It is Autumn')
    elif (input_day >= 21 and input_day <= 31):
        print('It is Winter')
    else:
        print('{} {} is not a valid date.'.format(input_month, input_day))

elif (input_month == 'January') and (0 < input_day <= 31):
    print('It is Winter')

elif (input_month == 'February') and (0 < input_day <= 29):
    print('It is Winter')

elif input_month == 'March':
    if (input_day <= 19) and (input_day > 0):
        print('It is Winter')
    else:
        print('{} {} is not a valid date.'.format(input_month, input_day))
else:
    print('{} {} is not a valid date.'.format(input_month, input_day))


