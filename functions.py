class Cell:
    def __init__(self, sub=None, fac=None, rm=None):
        self.sub = sub
        self.fac = fac
        self.rm = rm

    def __str__(self):
        atr = []
        if self.sub:
            atr.append(f"Subject: {self.sub}")
        if self.fac:
            atr.append(f"Faculty: {self.fac}")
        if self.rm:
            atr.append(f"Room: {self.rm}")
        return ', '.join(atr)


def create_table(dys, hrs):
    c = [[Cell() for _ in range(dys)] for _ in range(hrs)]
    return c


def print_table(table):
    for i in table:
        for j in i:
            k = j.sub
            if k:
                print('| '+k.center(10)+'|', end=' ')
            else:
                print('| '+' '.center(10)+'|', end=' ')
        print('\n')

def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


