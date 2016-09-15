#problem.py

#a 3SAT instance
#called problem and not instance because "instance" is a programming word

class Problem:
    def __init__(self):
        self.clauses = []
        self.comment_lines = []
        self.name = ""
        #file name convention:
        # {varcount}v.{clausecount}c.{a}.{b}.{c}.{gen}.yyyymmddh*m*.{batch_seq#}.{uuid}.cnf
        # a = highest count of a literal  (should be v_0) -- hexadecimal
        # b = floor( average of count of literal ) -- hexadecimal
        # c = lowest count of literal (should be !v_(n-1) -- hexadecimal
        # gen = generator name, e.g. "sim" -- avoid "s" and "u"
        # h* = hour of day, 0,1..m,n for hours 0 to 23
        # m* minutes / 4    -- hexadecimal (it will fit)
        # batch_seq# - sequence number in batch, e.g. "120" for #120 out of 500
        # uuid - uuid generated in whatever standard
        # cnf or json, maybe a binary format, etc

    def add(self, clause):
        self.clauses.append(clause)


    def __eq__(self, other):
        '''
        Warning:  naiive and brute force equality implementation

        It is possible to have two Problems with identical structure that will
        still return false (i.e. graph isomorphism problem not solved here)

        :param other:
        :return:
        '''
        if len(self.clauses) != len(other.clauses):
            return False

        self.clauses = sorted(self.clauses)
        other.clauses = sorted(other.clauses)

        for i in range(len(self.clauses)):
            if self.clauses[i] != other.clauses[i]:
                return False

        return True




    def to_cnf(self):
        return ""

    @staticmethod
    def from_cnf(cnf_str):
        p = Problem()
        return p

    #TODO: need an equals() method useful enough for a unit test