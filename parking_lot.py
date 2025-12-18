from parking_slot import ParkingSlot

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.slots = [ParkingSlot(i + 1) for i in range(capacity)]

    def park_vehicle(self, vehicle):
        for slot in self.slots:
            if not slot.is_occupied:
                slot.park(vehicle)
                return slot.slot_id
        return -1

    def remove_vehicle(self, vehicle_number):
        for slot in self.slots:
            if slot.is_occupied and slot.vehicle.number == vehicle_number:
                slot.remove_vehicle()
                return True
        return False

    def available_slots(self):
        return [slot.slot_id for slot in self.slots if not slot.is_occupied]

    def status(self):
        result = []
        for slot in self.slots:
            if slot.is_occupied:
                result.append(
                    (slot.slot_id, slot.vehicle.number, slot.vehicle.vehicle_type)
                )
        return result
