## The Single Responsibility Principle(SRP)

### The SRP states that "a class, function or a module should have one and only one reason to change." This means a class should only have a single job that defines it. For example, a class is responsible in retrieving users from the database, it should only retrieve the users and should not care about formatting the data or displaying it to the users. This should be handled by another class/module. the SRP design principle can be compared to the concept of a clean, well organized room. Having utensil/clothes all over the room is messy, and this is a representation of spaghetti code. Everything should be put where it belongs and easier to find whenever any new person steps into the room.

### The program below defines a simple Animal class with its properties.
