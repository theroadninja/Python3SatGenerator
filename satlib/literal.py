


class Literal:
    TF = { True : "T", False : "F"}

    def __init__(self, variable, bool):
        self.variable = variable
        self.bool = bool

    def __str__(self):
        return "{}{}".format(self.variable, Literal.TF[self.bool])