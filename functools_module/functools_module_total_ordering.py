from functools  import total_ordering



@total_ordering
class Employee:
    def __init__(self, id_card, name):
        self.id_card = id_card
        self.name = name


    def __eq__(self, other):
        if self.__class__ is not other.__class__ :
            return NotImplemented
        return self.id_card == other.id_card
    

    def __gt__(self, other):
        if self.__class__ is not other.__class__ :
            return NotImplemented
        return self.id_card > other.id_card 



p1 = Employee('125346', 'charlie')
p2 = Employee('945435', 'katty')


print(p1 == p2)
print(p1 != p2)
print(p1 < p2)
print(p1 > p2)
