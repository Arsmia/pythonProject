what = input('which sing do you want to choose?')
a = int(input('please, write first number'))
b = int(input('please, write second number'))

if what == '+':
    c = a + b
    print('answer' + str(c))
elif what == '-':
    c = a - b
    print('answer' + str(c))
elif what == '/':
    c = a / b
    print('answer' + str(c))
elif what == '*':
    c = a * b
    print('answer' + str(c))
else:
    print('error')