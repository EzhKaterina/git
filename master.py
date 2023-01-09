def expression_result(expression):
    rez = 0
    for i in range(len(expression)):
        if expression[i] == "^":
            pl = expression.find("*")
            sum = int(expression[pl+1:i]) ** int(expression[i:-1])
            doPl = int(expression[:pl])
            rez = doPl * sum
            break
    return rez

    expression = "-2+x^1-3*x^2+x^2+100*x^3-2*x"  
    x = 0  

    rez = 0
    numsList = []
    symbolsList = []

    if expression[0] == "-":
        startIndex = 1

    while len(expression) > 0:
        for i in range(startIndex, len(expression)):
            if expression[i] in "-+":
                startIndex = i + 1
                numsList.append(expression_result(expression[:i-1]))
                symbolsList.append(expression[i])

    for i in range(len(numsList)):
        for j in range(len(symbolsList)):
            if j == 0 and symbolsList[j+1] == "+":
                rez += int(numsList[i]) + int(numsList[i+1])
            elif j == 0 and symbolsList[j+1] == "-":
                rez += int(numsList[i]) - int(numsList[i + 1])
            elif j == "+":
                rez += int(numsList[i+1]) + int(numsList[i+2])
            elif j == "-":
                rez += int(numsList[i + 1]) - int(numsList[i + 2])

    print(rez)
