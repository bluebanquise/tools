import os
import yaml
import subprocess
import shutil


def load_yaml(filename):
#    logging.info(bcolors.OKBLUE+'Loading YAML '+filename+bcolors.ENDC)
    with open(filename, 'r') as f:
        # Select YAML loader (needs PyYAML 5.1+ to be safe)
        if int(yaml.__version__.split('.')[0]) > 5 or (int(yaml.__version__.split('.')[0]) == 5 and int(yaml.__version__.split('.')[1]) >= 1):
            return yaml.load(f, Loader=yaml.FullLoader)
        return yaml.load(f)

def dump_yaml(filename,yaml_data):
#    logging.info(bcolors.OKBLUE+'Dumping YAML '+filename+bcolors.ENDC)
    with open(filename, 'w') as f:
        f.write(yaml.dump(yaml_data))
    return 0


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

        try:
            stdout, stderr = subprocess.Popen("tar -C /dev/shm -xOJf " + b_image_path + " bluebanquise_image_metadata.yml", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True).communicate()
            image_meta_data = yaml.safe_load(stdout)
            print("Loading image with following meta data: " + str(image_meta_data))
            os.mkdir("/var/lib/bluebanquise-diskless/bootstrapper_images/" + image_meta_data['image_name'])
            shutil.copy2(b_image_path, "/var/lib/bluebanquise-diskless/bootstrapper_images/" + image_meta_data['image_name'])
            dump_yaml("/var/lib/bluebanquise-diskless/bootstrapper_images/"+image_meta_data['image_name']+"/bluebanquise_image_metadata.yml", image_meta_data)

        except OSError as e:
            print("Execution failed:", e, file=stderr)

