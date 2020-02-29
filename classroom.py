import copy


class Classroom:
    def __init__(self, number, capacity, equipment):
        """
        Initialize classroom
        number: str
        capacity: int
        equipment: list
        """
        self.number = number
        self.capacity = capacity
        self.equipment = copy.copy(equipment)

    def __str__(self):
        """
        Returns Classroom in good representation for user
        """
        return 'Classroom {} has a capacity of {} persons and ' \
               'has the following equipment: {}.'.format(
                   self.number, str(self.capacity), ', '.join(self.equipment))

    def is_larger(self, room2):
        """

        Classroom, Classroom -> bool
        Returns True if first room have bigger capacity then second room
        """
        return self.capacity > room2.capacity

    def equipment_differences(self, room2):
        """

        Classroom, Classroom -> list
        Returns the equipment in first room which is missing in second
        """
        return sorted(list(set(self.equipment).difference(room2.equipment)))

    def __repr__(self):
        """

        Returns beautiful representation for programmer
        """
        return "Classroom('{}', {}, {})".format(self.number, self.capacity,
                                                str(self.equipment))


if __name__ == '__main__':
    classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = Classroom('007', 12, ['TV'])
    print(classroom_016.is_larger(classroom_007))
    print(classroom_016.equipment_differences(classroom_007))
    print(classroom_016.__repr__())
