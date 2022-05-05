import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, value in kwargs.items():
            self.color = color
            self.value = value
            for i in range(self.value):
                self.contents.append(self.color)
            self.removed = []

    def draw(self, number):
        if number <= len(self.contents):
            for i in range(number):
                c = random.choice(self.contents)
                self.removed.append(str(c))
                self.contents.remove(c)
            return self.removed
        else:
            for i in self.removed:
                self.contents.append(i)
            self.removed = []
            return False


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiments = []
    for color, value in expected_balls.items():
        for i in range(value):
            experiments.append(color)

    M = 0

    for N in range(num_experiments):
        hat.draw(num_balls_drawn)
        drawn = copy.copy(hat.removed)
        count = 0
        for i in experiments:
            if i in drawn:
                count += 1
                drawn.remove(i)
        if count == len(experiments):
            M += 1

    probability = (M / num_experiments)
    if probability == 0.0:
        probability = 1.0
    else:
        probability -= 0.1

    return probability


chat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
prob = experiment(hat=chat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
print(prob)
