class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Woof!"


class Canine:
    def run(self):
        return "Running fast!"


class Cat:
    def meow(self):
        return "Meow!"


class DogMulti(Canine, Cat):
    def bark(self):
        return "Woof!"


class Grandparent:
    def family_name(self):
        return "Smith"


class Parent(Grandparent):
    def parent_name(self):
        return "John"


class Child(Parent):
    def child_name(self):
        return "Mike"


class Vehicle:
    def move(self):
        return "Moving!"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bike(Vehicle):
    def ride(self):
        return "Riding a bike"


class Base:
    def base_method(self):
        return "Base method"


class A(Base):
    def method_a(self):
        return "Method A"


class B(Base):
    def method_b(self):
        return "Method B"


class C(A, B):
    def method_c(self):
        return "Method C"


class X:
    def show(self):
        return "X"


class Y(X):
    def show(self):
        return "Y"


class Z(X):
    def show(self):
        return "Z"


class A_MRO(Y, Z):
    pass


def show_mro():
    print(A_MRO.mro())


def main_menu():
    while True:
        print("\nTanlang:")
        print("1. Single Inheritance")
        print("2. Multiple Inheritance")
        print("3. Multilevel Inheritance")
        print("4. Hierarchical Inheritance")
        print("5. Hybrid Inheritance")
        print("6. Method Resolution Order")
        print("0. Chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == '1':
            dog = Dog()
            print(dog.speak())
            print(dog.bark())

        elif choice == '2':
            dog_multi = DogMulti()
            print(dog_multi.run())
            print(dog_multi.meow())

        elif choice == '3':
            child = Child()
            print(child.family_name())
            print(child.parent_name())
            print(child.child_name())

        elif choice == '4':
            car = Car()
            print(car.move())
            print(car.drive())

            bike = Bike()
            print(bike.move())
            print(bike.ride())

        elif choice == '5':
            hybrid = C()
            print(hybrid.base_method())
            print(hybrid.method_a())
            print(hybrid.method_b())
            print(hybrid.method_c())

        elif choice == '6':
            show_mro()

        elif choice == '0':
            print("Chiqish...")
            break

        else:
            print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")


if __name__ == "__main__":
    main_menu()
