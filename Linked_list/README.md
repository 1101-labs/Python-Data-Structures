# MiniLinkedList — Building a Linked List from Scratch

## Overview

MiniLinkedList is a beginner Python project that implements a singly linked list from scratch using classes, objects, and references.

The goal is to understand how linked lists work internally instead of relying on Python's built-in data structures.

## What Is a Linked List?

A linked list is a data structure made up of nodes. Each node stores:

- **Data** — the value held by the node.

- **Next** — a reference to the next node in the list.

The list starts at a reference called `head`, which points to the first node.

Example:

```
head ↓[10 | next] → [20 | next] → [30 | None]
```

Unlike a Python list, the nodes do not need to be stored next to each other in memory. Each node connects to the next through a reference.

## Features

- **Append** — add a new value to the end of the list.

- **Display** — traverse and display the values in the list.

- **Length** — determine how many nodes are in the list.

- **Contains** — check whether a value exists in the list.

- **Remove** — remove a node containing a specified value.

## Concepts Practiced

This project helps develop an understanding of:

- Python classes and objects.

- Constructors using `__init__`.

- Instance attributes and object references.

- The relationship between nodes.

- Traversing a linked list using loops.

- Conditional statements and handling special cases.

- Functions, parameters, and return values.

- Boolean values (`True` and `False`).

- Modifying references to add and remove nodes.

- Handling an empty list and other edge cases.

## Project Structure

```
MiniLinkedList/├── main.py└── README.md
```

The filenames may differ depending on how the project is organized.

## How It Works

### 1. Node

The `Node` class represents an individual element in the linked list. Each node stores a value and a reference to the next node.

### 2. MiniLinkedList

The `MiniLinkedList` class manages the nodes. It maintains the head reference and provides methods for adding, searching, counting, displaying, and removing values.

### 3. Traversal

To visit the nodes, a temporary reference moves from one node to the next until it reaches `None`.

### 4. Removing Nodes

Removing a node requires changing references so that the previous node points to the node after the one being removed. Removing the head requires updating the head reference itself.

## How to Run

Open a terminal inside the project directory and run:

```
python3 main.py
```

If your main Python file has a different name, replace `main.py` with that filename.

## Learning Goals

The main objective is to understand how a linked list works internally, especially how references connect objects and how changing those references changes the structure of the list.

This project is part of a broader journey toward implementing data structures from scratch and understanding their behavior, efficiency, and trade-offs.


