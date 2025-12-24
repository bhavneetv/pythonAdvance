class dad:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("This is dad with greet method")

class child(dad):
    def __init__(self , name):
        self.name = name

        # Override
    def greet(self):
        print("This is child with greet method")


if __name__ == '__main__':
    dad1 = dad("father")
    print(dad1.name)
    dad1.greet()

    child = child("child")
    print(child.name)
    child.greet()

