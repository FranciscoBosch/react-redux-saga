input1 = raw_input("Enter your input value: ")

input2 = input1.split(" ")
digits = []
output = []
char  =[]
againDigit = False
againChar = False
for x in input2:
    if againDigit:
        digits.sort()
        output.append(digits)
        digits = []
    if againChar:
        char.sort()
        output.append(char)
        char = []
    if x.isdigit():
        digits.append(x)
        againDigit = True
    else:
        char.append(x)
        againChar = True


print (output)
