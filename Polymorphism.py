#Overridding Example

class A:

    def show(self):
        print('Show From A')

class B(A):

    def show(self):
        super().show()
        print('Show From B')

class C(B):

    def show(self):
        super().show()
        print('Show From C')

c1=C()
c1.show()

#Overloading Is not support in python So Defination keep in your mind....
'''
-Compile time polymorphism
    -Method overloading
    -When there is a more than one method in a single class having the same name but with different number of arguments
    - and their datatypes than it is called method overloading.
'''
