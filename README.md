# parking-system
# Parking Lot System (DSA + OOP Project)

## Description
This project implements a **Parking Lot System** using core **Data Structures and Algorithms (DSA)** along with **Object-Oriented Programming (OOP)** principles.

The system efficiently manages vehicle parking, spot allocation, ticket generation, and fee calculation with constant-time operations.

---

## Features

- Park and unpark vehicles
- Supports Bike, Car, and Truck
- Different parking spot sizes
- Automatic ticket generation
- Parking fee calculation
- Real-time parking status display

---

## Data Structures Used

- Hash Map (Dictionary)
- Lists
- UUID for ticket generation

---

## OOP Concepts Used

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Single Responsibility Principle

---

## Class Design Overview

### Vehicle (Base Class)
- Bike
- Car
- Truck

### ParkingSpot
- Stores spot size and availability

### Ticket
- Tracks entry time and assigned spot

### ParkingLot
- Core controller class
- Handles parking, unparking, and pricing

---

## Parking Rules

| Vehicle | Allowed Spots |
|-------|---------------|
| Bike  | Small, Medium, Large |
| Car   | Medium, Large |
| Truck | Large |

---

## Fee Structure

- First hour: ₹20
- Every additional hour: ₹10

---


