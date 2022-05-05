class Category:
    def __init__(self, name):
        self.name = name.title()
        self.ledger = []
        self.balance = 0
        self.percentage_spent = 0
        self.withdrawn = 0

    def check_funds(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= amount
            self.withdrawn += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, description=f"Transfer to {category.name}")
            category.deposit(amount, description=f"Transfer from {self.name}")
            return True
        else:
            return False

    def __str__(self):
        line1 = str(self.name).center(30, '*') + '\n'
        line2 = ''
        total = 0
        for i in self.ledger:
            values = [c for c in i.values()]
            amount = float(values[0])
            total += amount
            amount = f'{amount:.2f}'
            description = values[1]
            new_description = description

            if len(description) > 23:
                new_description = ''
                for j in range(23):
                    new_description += str(description)[j]

            line2 += new_description + amount.rjust(30 - len(new_description)) + '\n'
        line3 = f'Total: {total:.2f}'
        output = line1 + line2 + line3
        return output


def create_spend_chart(categories):
    category_list = []
    category_value = []
    total_withdrawn = 0
    for category in categories:
        total_withdrawn += int(category.withdrawn)
    for category in categories:
        category_list.append(category)
        category_value.append((category.withdrawn / total_withdrawn) * 100)
    print(category_value)

    line = 'Percentage spent by category\n'
    for i in range(100, -1, -10):
        line += (str(i) + '|').rjust(4)
        for de in category_value:
            if i <= de:
                line += ' o '
            else:
                line += '   '
        line += ' \n'

    line += '    ' + '-' + '-' * (3 * len(category_list)) + '\n'
    # find maximum characters
    maxim = 0
    for i in category_list:
        if len(str(i.name)) > maxim:
            maxim = len(str(i.name))

    for z in range(maxim):
        line += '   '
        for i in range(len(category_list)):
            try:
                line += '  ' + str(category_list[i].name)[z]
            except IndexError:
                line += '   '

        line += '  \n'
    return line.rstrip('\n')


food = Category("Food")
entertainment = Category('Entertainment')
business = Category('Business')
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))
