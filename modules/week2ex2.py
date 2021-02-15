import os


def get_file_names(path , out):
    files = os.listdir(path)

    with open(str.join(out, ".txt"), 'w') as file_object:

        for line in files:
            file_object.write(str(line)+ '\n')


def get_all_file_names(folderpath,out):
    lst = list()

    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            lst.append(filename)

    with open(str.join(out, ".txt"), 'w') as file_object:

        for line in lst:
            file_object.write(str(line)+ '\n')

def print_line_one(file_names):
    
    for file in file_names:
        with open(file) as f_obj:
            content = f_obj.readlines()

        for line in content[:1]:
            print(line)

def print_emails(file_names):

    for file in file_names:
        with open(file) as f_obj:
            content = f_obj.readlines()

        for line in content:
            if "init" in line:
                print(line)

def write_headlines(md_files, out=output.txt):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""

## get_file_names("./mynotebooks", "msg")
## get_all_file_names("./modules", "hej")
## print_line_one([".hejthejxhejt",".msgtmsgxmsgt"])
## print_emails([".hejthejxhejt",".msgtmsgxmsgt"])


