# class Parent(object):
#     def override(self):
#         print("PARENT override()")
#     def implicit(self):
#         print("PARENT implicit()")
#     def altered(self):
#         print("PARENT altered()")

# class Child(Parent):
#     def override(self):
#         print("CHILD override()")
#     def altered(self):
#         print("Child, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")

class Parent(object):
    def override(self):
        print("PARENT override()")
    def implicit(self):
        print("Implicit from Dad")
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("Child overrides whatever the parent has")
    def altered(self):
        print("Child, BEFORE PARENT is altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT has been altered")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


# most of the uses of inheritance cna be simplified or replaced with composition 
# multiple inheritance should be avoided at all costs
# The question of inheritance vs composition comes down to an attempt to solvethe problem of reusable code
# you DONT want duplicated code all over your software. CLEAN AND EFFICIENT IS KEY
# Use composition to package code into modules that are used in many diff unrelated place and situations
# Use inheritance only where there are clealy related reusable pieces of code that fit under a single common concept--or if you h
# have to because of something that you are using 
# all this being said, dont be a slave to these rules if you have no other choice
