def physics_formula_menu():
    print('\nPhysics formula option:')
    print('a. refractive index')
    print('b. number o images formed on by a mirror')
    print('c. electric force')
    print('d. magnification')
    print('e. electric field strength')

physics_formula_menu()

options = input('pick an option from a to e  ')
print(options)

if options == 'a':
    sin_i = int(input('Enter number  '))
    sin_r = int(input('Enter number  '))
    refractive_index = sin_i / sin_r
    print(refractive_index)

elif options == 'b':
    angle = int(input('Enter angle in degrees  '))
    number_of_images_formed_by_a_mirror = (360 / angle) - 1
    print(number_of_images_formed_by_a_mirror)

elif options == 'c':
    q1 = int(input('Enter value for q1  '))
    q2 = int(input('Enter value for q2  '))
    K = 9 * (10 ** 9)
    r =  int(input('Enter value for r  '))
    electric_force = (K * q1 * q2) / (r ** 2)
    print(electric_force)

elif options == 'd':
    image_height = int(input('enter image height  '))
    object_height = int(input('enter object height  '))
    magnification = image_height / object_height
    print(magnification)

elif options == 'e':
    force = int(input('enter force in newton  '))
    charge = int(input('enter charge   '))
    electric_field_strength = force * charge
    print(electric_field_strength)

else :
    print('invalid option an option from a to e')