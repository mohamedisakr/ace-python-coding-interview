# https://leetcode.com/problems/design-parking-system/description/?envType=problem-list-v2&envId=design&difficulty=EASY
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._parking_lot = [big, medium, small]

    # carType can be of three kinds: big, medium, or small,
    # which are represented by 1, 2, and 3 respectively
    # big -> 1
    # medium -> 2
    # small -> 3
    def addCar(self, carType: int) -> bool:
        if self._parking_lot[carType-1] > 0:
            self._parking_lot[carType-1] -= 1
            return True
        return False


parkingSystem = ParkingSystem(1, 1, 0)
# return true because there is 1 available slot for a big car
print(parkingSystem.addCar(1))
# return true because there is 1 available slot for a medium car
print(parkingSystem.addCar(2))
# return false because there is no available slot for a small car
print(parkingSystem.addCar(3))
# return false because there is no available slot for a big car. It is already occupied.
print(parkingSystem.addCar(1))
