import sys


class Car:
    def __init__(self, license_plate: str):
        self.license_plate = license_plate


class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.parked = []  # list of license plates

    def park(self, car: Car) -> bool:
        if len(self.parked) < self.capacity:
            self.parked.append(car.license_plate)
            return True
        return False

    def leave(self, license_plate: str) -> bool:
        if license_plate in self.parked:
            self.parked.remove(license_plate)
            return True
        return False

    def get_available(self) -> int:
        return self.capacity - len(self.parked)


def main() -> None:
    toks = sys.stdin.read().strip().split()
    if not toks:
        return
    it = iter(toks)

    try:
        capacity = int(next(it))
    except StopIteration:
        return

    try:
        n = int(next(it))
    except StopIteration:
        n = 0

    lot = ParkingLot(capacity)
    for _ in range(n):
        try:
            cmd = next(it)
        except StopIteration:
            break

        if cmd == 'park':
            try:
                plate = next(it)
            except StopIteration:
                break
            ok = lot.park(Car(plate))
            print('Parked' if ok else 'Full')
        elif cmd == 'leave':
            try:
                plate = next(it)
            except StopIteration:
                break
            ok = lot.leave(plate)
            print('Left' if ok else 'Car not found')
        elif cmd == 'status':
            print(f'Available: {lot.get_available()}')


if __name__ == '__main__':
    main()