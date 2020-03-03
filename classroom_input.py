import classroom


def read_classroom():
    """
     -> Classroom
    Read and create Classroom
    """
    number = input('Print classroom number: ')
    capacity = int(input('Print classroom capacity: '))
    text = 'Print equipment splited by spaces: '
    equipment = [x for x in input(text).split(' ')]
    return classroom.Classroom(number, capacity, equipment)


if __name__ == '__main__':
    classroom1 = read_classroom()
    print(classroom1)

    classroom2 = read_classroom()
    print(classroom2)

    if classroom1.is_larger(classroom2):
        print(classroom1.number + ' is larger')
    else:
        print(classroom2.number + ' is same or larger')
    print('Equipment difference: {}'.format(
        ' '.join(classroom1.equipment_differences(classroom2))))
    print('User representation: ' + str(classroom1))
    print('Programmer representation: ' + repr(classroom1))
