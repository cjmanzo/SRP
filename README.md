## The Liskov Substitution Principle (LSP)

### The LSP guide was introduced in 1987 by a computer scientist called Barbara Liskov during her conference on "Data abstraction". This principle is widely used in OOP related programming. The principle directs that an application should continue running without any bugs when a subclass inherits from a superclass. in simpler terms, when inheriting from the parent class, the parent class objects should behave the same way as the objects of a child-class.

### Take an example of a Rectangle class. A rectangle has 4 sides where 2 sides are equal. The area will be the product of the length and width. The same is true for a square since it too has 4 sides all equal. Methods from the Rectangle class can be used by the Square class application and still work without errors
