import classroom

if __name__ == '__main__':
    classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    assert classroom_016.number == '016'
    assert classroom_016.capacity == 80
    assert classroom_016.equipment == ['PC', 'projector', 'mic']
    assert str(classroom_016) == 'Classroom 016 has a capacity of 80 persons and has ' \
                                 'the following equipment: PC, projector, mic.'
    classroom_007 = classroom.Classroom('007', 12, ['TV'])
    assert classroom_016.is_larger(classroom_007)
    equipment_differences = classroom_016.equipment_differences(classroom_007)
    assert equipment_differences == ['PC', 'mic', 'projector']
    assert repr(classroom_016) == "Classroom('016', 80, ['PC', 'projector', 'mic'])"
