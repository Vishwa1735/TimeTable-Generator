class Cell:
    def __init__(self, subject=None, fac=None, rm=None):
        self.subject = subject
        self.fac = fac
        self.rm = rm

    def __str__(self):
        atr = []
        if self.subject:
            atr.append(f"subject: {self.subject}")
        if self.fac:
            atr.append(f"Faculty: {self.fac}")
        if self.rm:
            atr.append(f"Room: {self.rm}")
        return ', '.join(atr)


def create_table(dys, hrs):
    c = [[Cell() for _ in range(hrs)] for _ in range(dys)]
    return c

def print_table(table):
    for i in table:
        for j in i:
            k = j.subject
            if k:
                print('| '+k.center(12)+'|', end=' ')
            else:
                print('| '+' '.center(12)+'|', end=' ')
        print('\n')

def subject_frequency(subjects):
    l =[]
    for i in range(len(subjects)):
        l += [[subjects.Subject[i],subjects.Staff[i]]]*subjects.Frequency[i]
    return l


