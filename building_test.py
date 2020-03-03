import classroom
import building

if __name__ == '__main__':
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
    classrooms = [classroom_016, classroom_007, classroom_008]
    my_building = building.AcademicBuilding('Kozelnytska st. 2a', classrooms)
    assert my_building.address == 'Kozelnytska st. 2a'
    total_equipment = [('PC', 2), ('projector', 2), ('mic', 1), ('TV', 1)]
    assert total_equipment == my_building.total_equipment()
