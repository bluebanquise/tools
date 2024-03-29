# ██████╗ ██╗     ██╗   ██╗███████╗██████╗  █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗██╗███████╗███████╗
# ██╔══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔══██╗████╗  ██║██╔═══██╗██║   ██║██║██╔════╝██╔════╝
# ██████╔╝██║     ██║   ██║█████╗  ██████╔╝███████║██╔██╗ ██║██║   ██║██║   ██║██║███████╗█████╗
# ██╔══██╗██║     ██║   ██║██╔══╝  ██╔══██╗██╔══██║██║╚██╗██║██║▄▄ ██║██║   ██║██║╚════██║██╔══╝
# ██████╔╝███████╗╚██████╔╝███████╗██████╔╝██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝██║███████║███████╗
# ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝
#
# demo module:
#   A module to demonstate how to create customized diskless images classes.
#
# 1.3.0: Role update. David Pieters <davidpieters22@gmail.com>
# 1.2.0: Role update. David Pieters <davidpieters22@gmail.com>, Benoit Leveugle <benoit.leveugle@gmail.com>
# 1.1.0: Role update. Benoit Leveugle <benoit.leveugle@gmail.com>, Bruno Travouillon <devel@travouillon.fr>
# 1.0.0: Role creation. Benoit Leveugle <benoit.leveugle@gmail.com>
#
# https://github.com/bluebanquise/bluebanquise - MIT license


# Import base modules
import os
import shutil
import logging

# Import diskless modules
from diskless.modules.base_module import Image
from diskless.image_manager import ImageManager
from diskless.utils import Color, printc, inform, ask, ok, select_from_list


class DemoImage(Image):
    """This module will allow you to understand how to create your own image class.\
       Images created with this class are not real diskless images."""

    # Class constructor
    # You can see that only name is a mandatory argument. To create an already existing image, call the constructor whith only the image name.
    # To create a new image you must enter all arguments.
    #                                ↴                       ↴
    def __init__(self, name, my_message=None, useless_argument=None):
        super().__init__(name, my_message, useless_argument)

    #                               V             V  <- You can see the arguments relation
    # Create demo image             V             V
    def create_new_image(self, my_message, useless_argument):
        super().create_new_image()
        # Create the 'my_message attribute'
        self.my_message = my_message
        self.generate_files()
        ok("Image created ! Check images list to look at it.")

    def generate_files(self):
        super().generate_files()
        self.create_image_folders()
        self.generate_file_system()
        # The 'my_message attribute' will be saved in image_data file when registering.
        # You will see it when listing images after demo image creation.

    def create_image_folders(self):
        super().create_image_folders()
        # Create a folder just for the exemple.
        logging.debug('Executing \'mkdir -p /diskless/demo_directory_' + self.name + '\'')
        os.makedirs('/diskless/demo_directory_' + self.name)

    # This function will help us to understand the difference between clean and remove methods
    def generate_file_system(self):
        super().generate_file_system()

        # Create a file to remove
        logging.debug('Creating file /diskless/demo_file_to_remove_' + self.name + '.txt')
        f = open('/diskless/demo_file_to_remove_' + self.name + '.txt', 'a')
        f.write("This file will be removed throughout normal image generation !")
        f.close()

        ask('Would you like to corrupt this image generation?(yes/no)')
        choice = input('-->: ')
        if choice == 'yes':
            exit()  # <- Fake a program crash
        # Exiting without removed file_to_remove.txt file.
        # Therefore, the file will be removed by the clean method.
        elif choice != 'no':
            raise UserWarning('Not a valid input.')

        # Else, continue normal process...

        # Remove the file_to_remove file is the normal image creation process
        logging.debug('Executing \'rm -f /diskless/demo_file_to_remove_' + self.name + '.txt\'')
        os.remove('/diskless/demo_file_to_remove_' + self.name + '.txt')

    def remove_files(self):
        # Remove the image files when the image was properly created
        super().remove_files()

        logging.debug('Executing \'rm -rf /diskless/demo_directory_' + self.name + '\'')
        shutil.rmtree('/diskless/demo_directory_' + self.name)

    # Clone the image into another image
    def clone(self, clone_name):

        super().clone(clone_name)

        CLONE_IMAGE_DIRECTORY = Image.IMAGES_DIRECTORY + clone_name + '/'

        # Copying image directory for the clone
        logging.debug('Copying directory ' + self.IMAGE_DIRECTORY + ' into ' + CLONE_IMAGE_DIRECTORY)
        logging.debug('Executing \'cp -r ' + self.IMAGE_DIRECTORY + ' ' + CLONE_IMAGE_DIRECTORY + '\'')
        shutil.copytree(self.IMAGE_DIRECTORY, CLONE_IMAGE_DIRECTORY)

        # Create a clone object
        clone = DemoImage(clone_name)

        # Change the clone attribute values
        clone.name = clone_name
        clone.IMAGE_DIRECTORY = Image.IMAGES_DIRECTORY + clone_name + '/'

        # Register the clone to update it's image_data file values
        clone.register_image()

    # Clean all image files without image object when an image is corrupted
    @staticmethod
    def clean(image_name):
        Image.clean(image_name)

        # Cleaning image base directory
        if os.path.isdir(Image.IMAGES_DIRECTORY + image_name):
            logging.debug(Image.IMAGES_DIRECTORY + image_name + ' is a directory')
            logging.debug('Executing \'rm -rf ' + Image.IMAGES_DIRECTORY + image_name + '\'')
            shutil.rmtree(Image.IMAGES_DIRECTORY + image_name)

        # Cleaning all other related files and directories...
        if os.path.isdir('/diskless/demo_directory_' + image_name):
            logging.debug('/diskless/demo_directory_' + image_name + ' is a directory')
            logging.debug('Executing \'rm -rf /diskless/demo_directory_' + image_name + '\'')
            shutil.rmtree('/diskless/demo_directory_' + image_name)

        # We need to try to delete the demo_file.txt file in the clean method.
        # In fact the generation of the demo image can be halted before that the
        # normal process of DemoImage image creation removed demo_file.txt.
        if os.path.isfile('/diskless/demo_file_to_remove_' + image_name + '.txt'):
            logging.debug('/diskless/demo_file_to_remove_' + image_name + '.txt is a file')
            logging.debug('Executing \'rm -f /diskless/demo_file_to_remove_' + image_name + '.txt\'')
            os.remove('/diskless/demo_file_to_remove_' + image_name + '.txt')

    @staticmethod
    def get_boot_file_template():
        """Get the class boot file template.
        This method must be redefined in all Image subclasses."""
        return 'Useless bootfie content'


#####################
# CLI reserved part #
#####################

def cli_menu():
    """This method is needed for all diskless module to be available by cli interface."""

    printc('\n == Welcome to demo image module == \n', Color.GREEN)

    ask('Select an action')
    action_list = ['Create my demo image']
    action = select_from_list(action_list)
    print('')

    if action == 'Create my demo image':

        # Condition to test if image name is compliant
        while True:

            ask('Give a name for your demo image')
            # Get new image name
            selected_image_name = input('-->: ').replace(" ", "")

            if selected_image_name == '':
                inform('Image name cannot be empty !')

            elif ImageManager.is_image(selected_image_name):
                inform('Image ' + selected_image_name + ' already exist, use another image name.')

            else:
                break

        ask('Give a message for your demo image:')
        demo_message = input('-->: ')

        # Create a DemoImage image
        DemoImage(selected_image_name, demo_message)
