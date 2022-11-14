class Chromosome:

    A = ""  # binary quantity
    X = 0  # normalized quantity
    q = 0  # output of this firm
    fitness = 0  # fitness of this firm

    def __str__(self):  # objeyi print edebilmek icin
        return f"A: {self.A} X = {self.X} q = {self.q} fitness = {self.fitness}"

    def __repr__(self):  # objeyi print edebilmek icin
        return f"A: {self.A} X = {self.X} q = {self.q} fitness = {self.fitness}"
