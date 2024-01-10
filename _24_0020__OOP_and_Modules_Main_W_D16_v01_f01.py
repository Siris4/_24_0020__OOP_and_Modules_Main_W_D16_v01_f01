# import another_module
from _24_0020__OOP_and_Modules_another_module_W_D16_v01 import another_variable



path = "_24_0020__OOP_and_Modules_another_module_W_D16_v01"

print(another_variable)

import turtle
#OR
from turtle import Turtle

# print(another_module)

# print the variable named "another_variable", which is inside the module named "another_module".
print(f"This is another way to port data over from another Module or Program: {another_variable}")

from turtle import Turtle
#does the EXACT same thing as below:
tiptup = turtle.Turtle()

#tiptup (Object) = #turtle(Module).Turtle(Class) (blue C is Class) () Parenthesis MUST be included to activate the combination of words before it.
tiptup = turtle.Turtle()
#is the same as:
tiptup = Turtle()
# understood as "tiptup equals a new Object, created from the Turtle Class, and it's constructed"

print(tiptup)  #NOT THE SAME AS PRINTING A STRING!!
#<turtle.Turtle object at 0x000001D511E7FF10>     (saved in the computer's memory)
#it is an actual Object that is being printed
turtle.mainloop()