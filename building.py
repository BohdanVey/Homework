import classroom


class AcademicBuilding:
    def __init__(self, address, classrooms):
        """
        Initizalize Academic Building
        address: str
        classrooms: list of Classrooms
        """
        self.address = address
        self.classrooms = classrooms

    def total_equipment(self):
        """
        AcademicBuilding-> list of tuple
        Return the amount of each equipment in building
        """
        dct = dict()
        for room in self.classrooms:
            for equipment in room.equipment:
                dct[equipment] = dct.get(equipment, 0) + 1

        equipment = [(i, dct[i]) for i in dct]
        return equipment

    def __str__(self):
        """
        Returns Classroom in good representation for user
        """
        to_print = self.address + '\n'
        for room in self.classrooms:
            to_print += str(room) + '\n'
        return to_print.strip()


if __name__ == '__main__':
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms = [classroom_016, classroom_007, classroom_008]
    building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    print(building.total_equipment())
    print(building)
