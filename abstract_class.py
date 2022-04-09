from abc import ABC, abstractmethod
class A :
    @abstractmethod
    def show(self):
        print('show from A')
    
    @abstractmethod
    def now(self):
        pass


class B(A):
    def show(self):
        super().show()
        print('show from B')

    def now(self):
        print('now from B')




b1 = B()
b1.show()
b1.now()
