#problem.py

#a 3SAT instance
#called problem and not instance because "instance" is a programming word

from clause import Clause

class Problem:
    def __init__(self):
        self.clauses = []
        self.comment_lines = []
        self.name = ""
        self.variables = set()

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
        for literal in clause.literals:
            self.variables.add(literal.variable)

    def addComment(self, comment):
        self.comment_lines.append(comment)

    def hasClause(self, clause):
        #TODO: slow.  need to use set to be fast
        for c in self.clauses:
            if c == clause:
                return True
        return False

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


    def var_count(self):
        return len(self.variables)

    def clause_count(self):
        return len(self.clauses)


    def to_cnf(self):
        lines = []
        for comment in self.comment_lines:
            lines.append(comment)

        pline = "p cnf {} {}".format(
            str(self.var_count()), str(self.clause_count()))
        lines.append( pline )

        for c in self.clauses:
            lines.append(c.to_cnf_line())

        return "\n".join(lines)

    @staticmethod
    def from_cnf(cnf_str):
        lines = cnf_str.splitlines()
        return Problem.from_cnf_lines(lines)


    @staticmethod
    def from_cnf_lines(lines):
        '''
        This maybe not be the canonical cnf format (e.g.  http://people.sc.fsu.edu/~jburkardt/data/cnf/cnf.html )
        I am not allowing multi-line clauses because that is fucking retarded.

        :param lines:
        :return:
        '''
        p = Problem()

        varcount = 0
        for line in lines:
            line = line.strip() #trim
            if line == "":
                continue
            elif "c" == line[0].lower():
                p.addComment(line)
            elif "p" == line[0].lower():
                #p {problem type} {varcount} {clausecount}
                _, problem_type, varcount, clausecount = line.split()
            else:
                numbers = [int(s) for s in line.split()]
                c = Clause.fromCnfArray(numbers)
                p.add(c)

        #TODO:  !!!!! normalize, and fix varcount

        #TODO:  useful exception handling?
        return p

    #TODO: need an equals() method useful enough for a unit test