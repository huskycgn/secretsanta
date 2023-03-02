from random import choice


class Santamat:
    def __init__(self, santalist):
        # We need to two lists for this to work.
        self.santalist = santalist
        self.beneficiarylist = santalist.copy()
        self.pairs = { }

    def getsantas(self):
        while len(self.santalist) > 0:

            secret_santa = choice(self.santalist)

            beneficiary = choice(self.beneficiarylist)

            while secret_santa.name == beneficiary.name:
                beneficiary = choice(self.beneficiarylist)
            self.pairs[ secret_santa ] = beneficiary
            self.santalist.remove(secret_santa)
            self.beneficiarylist.remove(beneficiary)
        return self.pairs


class Participant:
    '''Class for Participants'''
    def __init__(self, name, wish, mailadresse):
        self.name = name
        self.mailadresse = mailadresse
        self.wish = wish
