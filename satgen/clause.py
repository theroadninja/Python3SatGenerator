import literal

class Clause:
    def __init__(self, literals):
        if literals is None:
            raise ValueError("")
        _ = iter(literals) #make sure its iterable


        self.literals = literals

    def __str__(self):
        return "(" + " v ".join([str(x) for x in self.literals]) + ")"