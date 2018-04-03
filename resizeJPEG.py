import glob
import subprocess
import sys
import os

def resizeIMG(pre_path, new_path, image_path):
    bash_command = "convert " + pre_path + image_path + " -resize 256x256  " + new_path + image_path
    # print(bash_command)
    process = subprocess.Popen(bash_command.split())
    output, error = process.communicate()
    if (error):
        return 0
    else:
        return 1

if __name__ == '__main__':   
    pre_path = "Dataset_Combined/"
    new_path = "Dataset_resized/"
    image_files = glob.glob(pre_path + '*.jpg')
    print(str(len(image_files)) + ' .jpg files found to adjust')
    # print(image_files[0] + " image file")
    success_count = 0
    for image_file in image_files:
        # possible_xml_file = image_file.split('.')[0] + '.xml'
        # xml_path = os.getcwd() + '/' + possible_xml_file
        # print(xml_path)
        if (os.path.exists(image_file)):
            # print('Path exists:' + new_image_path + " | adding new image path for " + sys.argv[1])
            image_file_name = image_file.rsplit('/',1)[1]
            print(image_file_name)
            print("Image file: " + pre_path + " " + image_file_name)
            success_count += resizeIMG(pre_path, new_path, image_file_name)

    print('Resized and/or moved: ' + str(success_count) + ' images, out of ' + str(len(image_files)) + ' .jpeg files')

    #         # path.text = str(new_image_path)
    #         # tree.write(pre_path + xml_path)
    #         return 1
    #     else:
    #         print('New image path not found for ' + new_image_path)
    #         return 0
     
    # resizeIMG(sys.argv[1], sys.argv[2], sys.argv[3])