import building
import classroom_test

if __name__ == '__main__':
    address = input('Address: ')
    number_of_rooms = input('Print number of rooms: ')
    classrooms = []
    for i in range(int(number_of_rooms)):
        classroom = classroom_test.read_classroom()
        print(classroom)
        classrooms.append(classroom)
    main_building = building.AcademicBuilding(address, classrooms)
    print(main_building.total_equipment())
    print(main_building)
