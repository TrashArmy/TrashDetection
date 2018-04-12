import sys
import os
import xml.etree.ElementTree as ET
import glob
import subprocess

def correctPath(pre_path, xml_path):
    tree = ET.parse(pre_path + xml_path)
    root = tree.getroot()
    for path in root.iter('path'):
        identified_image_file = xml_path.split('.')[0] + '.jpg'
        new_image_path = os.getcwd() + '/' + pre_path + identified_image_file
        if (os.path.exists(new_image_path)):
            # print('Path exists:' + new_image_path + " | adding new image path for " + sys.argv[1])
            path.text = str(new_image_path)
            tree.write(pre_path + xml_path)
            return 1
        else:
            print('New image path not found for ' + new_image_path)
            return 0

# pre_path = 'Dataset_Combined/' 

if __name__ == '__main__':
    xml_files = glob.glob(sys.argv[1] + '*.xml')
    print(str(len(xml_files)) + ' .xml files found to adjust')
    success_count = 0
    for xml_file in xml_files:
        # success_count += correctPath
        success_count += correctPath('', xml_file)
    
    print('Adjusted: ' + str(success_count) + ' paths, out of ' + str(len(xml_files)) + ' xml files')

    # for xml_file in xml_files
    # for
    # correctPath('Dataset_Combined/',)
            
    # prePath = sys.argv[1]
    # image_files = glob.glob(sys.argv[1] + '*.jpg')
    # print(str(len(image_files)) + ' .jpg files found to adjust')
    # success_count = 0
    # for image_file in image_files:
    #     possible_xml_file = image_file.split('.')[0] + '.jpg'
    #     xml_path = os.getcwd() + '/' + pre_path + possible_xml_file
    #     if (os.path.exists(xml_path)):
    #         # print('Path exists:' + new_image_path + " | adding new image path for " + sys.argv[1])
    #         resizeIMG(pre_path, sys.argv[2], image_file)
    #         # path.text = str(new_image_path)
    #         # tree.write(pre_path + xml_path)
    #         return 1
    #     else:
    #         print('New image path not found for ' + new_image_path)
    #         return 0

    # resizeIMG(sys.argv[1], sys.argv[2], sys.argv[3])