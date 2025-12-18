from vehicle import Vehicle
from parking_lot import ParkingLot

parking_lot = ParkingLot(capacity=5)

while True:
    print("\nParking Lot Menu")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. View Available Slots")
    print("4. View Parking Status")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        number = input("Vehicle Number: ")
        vtype = input("Vehicle Type (Car/Bike): ")
        vehicle = Vehicle(number, vtype)
        slot = parking_lot.park_vehicle(vehicle)
        print("Parked at slot" if slot != -1 else "Parking Full", slot)

    elif choice == "2":
        number = input("Vehicle Number: ")
        print("Removed" if parking_lot.remove_vehicle(number) else "Not Found")

    elif choice == "3":
        print("Available Slots:", parking_lot.available_slots())

    elif choice == "4":
        print("Occupied Slots:", parking_lot.status())

    elif choice == "0":
        break
