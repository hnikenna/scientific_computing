
def arithmetic_arranger(problems, solve=False):
    solution = ''
    top, bot, bord, soln = [], [], [], []
    arranged_problems = ''
    for question in problems:
        if len(problems) > 5:
            return "Error: Too many problems."
        topFigure, operator, bottomFigure = question.split()
        if not topFigure.isdecimal() or not bottomFigure.isdecimal():
            return "Error: Numbers must only contain digits."
        if len(topFigure) > 4 or len(bottomFigure) > 4:
            return "Error: Numbers cannot be more than four digits."
        topValue = '  ' + topFigure.rjust(max(len(topFigure), len(bottomFigure)))
        bottomValue = operator + ' ' + (bottomFigure.rjust(max(len(topFigure), len(bottomFigure))))
        border = "-" * (max(len(topFigure), len(bottomFigure)) + 2)
        if solve:
            if operator == '+':
                solution = int(topFigure) + int(bottomFigure)
            if operator == '-':
                solution = int(topFigure) - int(bottomFigure)
            solution = str(solution).rjust(max(len(topFigure), len(bottomFigure)) + 2)
            soln.append(solution)
        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        solution = str(solution).rjust((max(len(topFigure), len(bottomFigure)) + 2))
        top.append(topValue)
        bot.append(bottomValue)
        bord.append(border)
    if soln:
        elements = [top, bot, bord, soln]
    else:
        elements = [top, bot, bord]
    count = 0
    for location in elements:
        count += 1
        subcount = 0
        for value in location:
            subcount += 1
            if subcount == len(location):
                arranged_problems += str(value)
                break
            arranged_problems += str(value) + '    '
        if count != len(elements):
            arranged_problems += '\n'
    return arranged_problems


print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))
