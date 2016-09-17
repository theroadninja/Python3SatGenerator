


class Lit:
    TF = { True : "T", False : "F"}
    to_bool = { True: True, False: False, "True": True, "False": False, "T" : True, "F" : False, "t" : True, "f" : False }

    def __init__(self, variable, bool=None):
        #simulate a second constructor Lit(i) that takes a positive/negative i, as if from cnf
        '''

        :param variable:
        :param cleanOneBased: fix input by translating to zero-based.  cannot be set if bool is passed
        :param bool:
        '''
        if bool is None:
            bool = (variable >= 0)
            variable = abs(variable)
        elif variable < 0:
                raise "variable cannot be < 0 if boolean provided"

        self.variable = variable
        self.bool = Lit.to_bool[bool]

    def __eq__(self, other):
        '''
        >>> Lit(0) == Lit(0, True)
        True
        >>> Lit(0) == Lit(0, False)
        False
        >>> Lit(5) == Lit(5, True)
        True
        >>> Lit(-5) == Lit(5, False)
        True
        >>> Lit(0, False) == Lit(0, False)
        True
        >>> Lit(0, False) == Lit(0, True)
        False
        >>> Lit(0, False) == Lit(1, False)
        False

        >>> Lit(2, False) == Lit(2, "F")
        True
        >>> Lit(2, True) == Lit(2, "T")
        True

        :param other:
        :return:
        '''
        return self.variable == other.variable and self.bool == other.bool

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __cmp__(self, other):
        '''
        Comparison function for programmers

        functools.cmp_to_key() to use with python3 bullshit
        See https://docs.python.org/3/library/stdtypes.html#list.sort

        >>> Lit(0, False).__cmp__(Lit(0, False))
        0
        >>> Lit(0, False) < Lit(0, False)
        False
        >>> Lit(0, True) < Lit(0, False)
        True
        >>> Lit(0, False) < Lit(1, False)
        True
        >>> Lit(0, False) < Lit(1, True)
        True
        >>> Lit(9, False) < Lit(1, True)
        False

        :param other:
        :return:
        '''
        if self.variable != other.variable:
            return self.variable - other.variable

        #normally int(True)=1 and int(False)=0, but I want True to have priority
        i = int(self.bool) ^ 1
        j = int(other.bool) ^ 1
        return i - j

    def __str__(self):
        return "{}{}".format(self.variable, Lit.TF[self.bool])

    def to_cnf(self):
        i = self.variable + 1 #convert to one based
        if not self.bool:
            i = i * -1
        return str(i)

    @staticmethod
    def fromCnf(i):
        flag = (i > 0)
        variable = abs(i) - 1 #convert to zero-based index
        return Lit(variable, flag)