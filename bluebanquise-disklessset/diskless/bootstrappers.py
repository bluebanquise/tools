import os
import yaml
def bootstrappers_main_menu():
    print("Select action:")
    print("1 List bootstrapper images")
    print("2 import bootstrapper image")
    print("3 delete bootstrapper image")

    main_action = input('-->: ')

    if main_action == '2':
        print('Please set path to tar.xz file:')
        b_image_path = input('-->: ')
        print('Opening file ' + b_image_path + ' ...')
        os.system('tar -C /dev/shm -xOJf ' + b_image_path + ' bluebanquise_image_metadata.yml')





def coucou():
    print("coucou")