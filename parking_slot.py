class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_occupied = False
        self.vehicle = None

    def park(self, vehicle):
        self.vehicle = vehicle
        self.is_occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.is_occupied = False
