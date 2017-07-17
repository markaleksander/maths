number = int(input("Enter number:\n"))
number_sum = sum([int(i) for i in list(str(number))])
if number % number_sum == 0:
    print('Sum of digits of {} is {}. {} is a Harshad number'.format(number, number_sum, number))
else:
    print('Sum of digits of {} is {}. {} is not a Harshad number'.format(number, number_sum, number))
