import os
import zipfile
import python2exeAPI
import shutil
import re
import sys
import requests
import shutil
import time
import os
import urllib2
import urllib

CODE = 2935


def upload(email, project_dir, main_script_name, destination, filename, platform=None, one_file=False, program_icon=None, show_console=False,
           dump_file=False, dump_file_email=None, is_zipped=False, test=False):

    # add the .zip file ext to the file name if it does note already exist
    if not filename.endswith(".zip"):
        filename += ".zip"

    print "process began"

    if platform is None:
        platform = [1]

    if is_zipped is False:
        zip_name = str(int(time.time()))

        # zip project dir here and upload it to server
        shutil.make_archive(zip_name, 'zip', project_dir)
    else:
        zip_name = project_dir

    file_dict = {}

    try:
        file_dict['zip_file'] = open(os.path.abspath('') + '/' + zip_name + '.zip', 'rb')
    except IOError:
        file_dict['zip_file'] = open(zip_name + '.zip', 'rb')

    if program_icon is not None:
        file_dict['icon'] = open(program_icon, 'rb')

    if test is False:
        res = requests.post(
            url='http://cpsuperstore.pythonanywhere.com/en/py2exe/convert',
            data={
                'user_email': email,
                'script_name': main_script_name,
                'windows': "on",
                'linux': "off",
                'mac': "off",
                'one_file': one_file,
                'console': show_console,
                'dumpFile': dump_file,
                'dumpFileEmail': dump_file_email
            },
            files=file_dict
        )

        print "Upload Complete"

        code = res.url[str(res.url).rfind("/") + 1:]
        url = "http://cpsuperstore.pythonanywhere.com/py2exe/comp_get_status/{}".format(code)
        # print url

        print "waiting for conversion"

        while True:
            response = urllib2.urlopen(url)
            status = response.read()
            if status == "6":
                break

            time.sleep(1)

        print "Conversion complete"

        print "downloading from server"

        urllib.urlretrieve("http://cpsuperstore.pythonanywhere.com/static/py2exe/post_convert/{}.zip".format(code), filename)

        url = "http://cpsuperstore.pythonanywhere.com/py2exe/comp_set_status/{}/{}/{}".format(CODE, code, 7)
        urllib2.urlopen(url)
    else:
        print "Running Test Mode. Conversion Skipped."
        filename = zip_name + '.zip'
        # filename = "[CONVERTED]" + filename
    try:
        shutil.move(os.path.abspath('') + '/' + filename, destination)
        os.remove(os.path.abspath('') + '/' + zip_name + '.zip')
    except shutil.Error:
        pass
    except OSError:
        os.remove(zip_name + '.zip')

try:
    properties = eval(''.join(open(sys.argv[1]).readlines()))
except IndexError:
    print "Usage:"
    print "CreateBuild <JSON File>"
    quit()
    
ZIP_NAME = properties["zipName"]
FINAL_NAME = properties["finalName"]

SAVE_PATH = properties["dst"]  # + "/" + properties["finalName"]

include_dirs = properties["includeDirs"]
include_files = properties["includeFiles"]

for i in range(len(include_dirs)):
    include_dirs[i] = properties["projectPath"] + "/" + include_dirs[i]

for i in range(len(include_files)):
    include_files[i] = properties["projectPath"] + "/" + include_files[i]

print "Zipping Code To Be Converted"

zf = zipfile.ZipFile(ZIP_NAME + ".zip", "w")
for each_dir in include_dirs:
    for dirname, subdirs, files in os.walk(each_dir):
        zf.write(dirname, dirname.replace(properties["projectPath"], ""))
        for filename in files:
            zf.write(os.path.join(dirname, filename), os.path.join(dirname, filename).replace(properties["projectPath"], ""))

for each_file in include_files:
    zf.write(each_file, each_file.replace(properties["projectPath"], ""))


zf.close()

upload(
    email="christopher.rocks@bell.net",
    project_dir=os.getcwd() + "/" + ZIP_NAME,
    main_script_name=properties["mainScriptName"],
    destination=os.getcwd(),
    filename=FINAL_NAME,
    platform=properties["platform"],
    one_file=properties["oneFile"],
    program_icon=properties["programIcon"],
    show_console=properties["showConsole"],
    dump_file=properties["dumpFile"],
    dump_file_email=properties["dumpFileEmail"],
    is_zipped=True,
)

print "Conversion Ended"

if properties["deleteOldBuild"] == 1:
    print "Deleting Old Build If It Exists"
    try:
        shutil.rmtree(SAVE_PATH)
    except OSError:
        pass

print "Saving New Build"
os.makedirs(SAVE_PATH)

shutil.move(os.getcwd() + '/' + FINAL_NAME + ".zip", SAVE_PATH)
with zipfile.ZipFile(SAVE_PATH + "/" + FINAL_NAME + ".zip","r") as zip_ref:
    zip_ref.extractall(SAVE_PATH + "/" + FINAL_NAME)

print "Cleaning Up Some Extra Files"

try:
    os.remove(os.getcwd() + "/tmp.zip")
except OSError:
    pass

for dirpath, dirnames, filenames in os.walk(SAVE_PATH + "/" + FINAL_NAME + "/" + FINAL_NAME):
    for name in dirnames:
        path = dirpath + "/" + name
        path = re.sub("/" + FINAL_NAME, '', path, 1)
        os.makedirs(path)
    for name in filenames:
        path = dirpath + "/" + name
        path = re.sub("/" + FINAL_NAME, '', path, 1)
        shutil.move(dirpath + "/" + name, path)
    shutil.rmtree(SAVE_PATH + "/" + FINAL_NAME + "/" + FINAL_NAME)

print "Creating Dependencies"

dependencies = properties["dependencies"]

root_dir = SAVE_PATH + "/" + FINAL_NAME

for folder in dependencies["createDirectories"]:
    try:
        os.makedirs(root_dir + "/" + folder)
    except OSError:
        pass

for folder in dependencies["copyDirectory"]:
    try:
        shutil.copytree(folder, root_dir + "/" + dependencies["copyDirectory"][folder])
    except OSError:
        pass

for filename in dependencies["copyFile"]:
    shutil.copy(filename, root_dir + "/" + dependencies["copyFile"][filename])
