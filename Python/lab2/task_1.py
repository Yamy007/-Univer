from task_2 import function
function()


class Person:
    name = str()
    lastname = str()
    quality = 1 # quality = int()
    def __init__(self, name, lastname, quality):
        self.name = name
        self.lastname = lastname
        self.quality = quality

    def prints(self):
        list = [self.name, self.lastname, str(self.quality)]
        return str(' '.join(list))

    def __del__(self):
        list = [self.name, self.lastname]
        print('Good bye: ' + str(' '.join(list)))

if __name__ == '__main__':
    a = Person("Taras", "Loh", 20)
    b = Person("ola", "Lola", 30)
    c = Person("yamy", "__", 100)

    print(a.prints())
    print(b.prints())
    print(c.prints())
    del(a)
    input(">>>")
