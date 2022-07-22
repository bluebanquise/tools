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

def images_manager_main_menu():
    print("Select action:")
    print("1 Create nfs image")
    print("2 Create live image")
    print("3 Clone image")
    print("4 Clone and convert from nfs to live")
    print("5 Update/modify image")
    print("6 Delete image")

    main_action = input('-->: ')

    if main_action == '4':
        print("Image to clone and convert ?")
        nfs_image_name = input('-->: ')
        print("New image name")
        image_name = input('-->: ')

        def get_dir_size(path='.'):
            total = 0
            with os.scandir(path) as it:
                for entry in it:
                    if entry.is_file():
                        total += entry.stat().st_size
                    elif entry.is_dir():
                        total += get_dir_size(entry.path)
            return total

        nfs_image_size = get_dir_size("/diskless/" + nfs_image_name)
        print(nfs_image_size)

    if main_action == '1':
        print("Please select bootstrapper image to be used as source:")
        images_list = os.listdir("/var/lib/bluebanquise-diskless/bootstrapper_images/")
        for image in images_list:
            print(image)
        bimage_name = input('-->: ')
        print("Please enter image name")
        image_name = input('-->: ')

        print("creating image")
        image_meta_data = load_yaml("/var/lib/bluebanquise-diskless/bootstrapper_images/" + bimage_name + "/bluebanquise_image_metadata.yml")
        os.mkdir("/diskless/" + image_name)
        os.mkdir("/var/www/html/pxe/diskless/" + image_name)
        os.system("tar -xJf /var/lib/bluebanquise-diskless/bootstrapper_images/" + bimage_name + "/image.tar.xz -C /diskless/" + image_name)
        os.system("cp /diskless/"+image_name+"/boot/"+image_meta_data['kernel']+" /var/www/html/pxe/diskless/" + image_name)
        os.system("cp /diskless/"+image_name+"/boot/"+image_meta_data['initramfs']+" /var/www/html/pxe/diskless/" + image_name)
   
        boot_file_content = '''#!ipxe
echo |
echo | Entering diskless/{image_name}/boot.ipxe
echo |
set image-kernel {image_kernel}
set image-initramfs {image_initramfs}
echo | Now starting staging nfs image boot.
echo |
echo | Parameters used:
echo | > Image target: {image_name}
echo | > Console: ${{eq-console}}
echo | > Additional kernel parameters: ${{eq-kernel-parameters}} ${{dedicated-kernel-parameters}}
echo |
echo | Loading linux ...
kernel http://${{next-server}}/pxe/diskless/{image_name}/${{image-kernel}} initrd=${{image-initramfs}} selinux=0 text=1 root=nfs:${{next-server}}:/diskless/{image_name}/,vers=4.2,rw rw ${{eq-console}} ${{eq-kernel-parameters}} ${{dedicated-kernel-parameters}} rd.net.timeout.carrier=30 rd.net.timeout.ifup=60 rd.net.dhcp.retry=4 {image_kernel_parameters}
echo | Loading initial ramdisk ...
initrd http://${{next-server}}/preboot_execution_environment/diskless/kernels/${{image-initramfs}}
echo | ALL DONE! We are ready.
echo | Booting in 4s ...
echo |
echo +----------------------------------------------------+
sleep 4
boot
'''.format(image_name=image_name, image_kernel=image_meta_data['kernel'], image_initramfs=image_meta_data['initramfs'], image_kernel_parameters=image_meta_data['kernel_parameters'])

        with open('/var/www/html/pxe/diskless/'+image_name+'/boot.ipxe', "w") as ff:
            ff.write(boot_file_content)


