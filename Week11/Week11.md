# Week 11 (14 Jan)

- Object-Oriented Programming: Introduction to Java
- Algorithms: Union-find
- LeetCode: Union-find


## Object-Oriented Programming (OOP)

Object-oriented programming is centred around creating classes and objects.

- A class is a description of what an object is and does.
- An object is an instance of a class.

```java
public class Person {
    // Attributes
    private int age;
    private String name;


    // Constructor
    public Person(int age, String name) {
        this.age = age;
        this.name = name;
    }

    // Methods
    public String getIntroduction() {
        return "My name is " + name + " and I am " + age + " years old.";
    }
    
    // Main method
    public static void main(String[] args) {
        Person alice = new Person(20, "Alice");
        System.out.println(alice.getIntroduction());
    }
}
```


## Algorithms

### Data structure vs Abstract Data Type

A queue requires the following interface (i.e. list of methods):
- `enqueue(item)`
- `dequeue(item)`
- `is_empty()`
- `count()`

There are many ways we can implement this interface:
- we can use an array; or
- we can use a linked list.

Here, a queue is a kind of _abstract data type_ (ADT). When describing an ADT, we often define a list of behaviours that it should provide, from the perspective of a user.

On the contrary, an array or linked list is a _data structure_. It is a concrete representation of data that can be used to implement an ADT.


### Union-find

Union-find is an ADT that
- categorises objects into different sets; and
- allows us to determine whether two given objects belong to the same set.

It requires the following interface:
- `union(a, b)`: Connects objects `a` and `b`.
- `find(a, b)`: Are `a` and `b` in the same "group"?



## LeetCode: Union-find

- [Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)
- [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)


### Correction: Max Area of Island

In the session, I mentioned that the best way to solve Max Area of Island with union-find is to map each cell's position to a unique integer. This is incorrect - it would be much more elegant to use a hash map/ dictionary instead! See `MaxAreaOfIsland.py`.