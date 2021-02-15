import argparse

parser = argparse.ArgumentParser(description = "write to file")
parser.add_argument('path', type=str, help='path to file')
parser.add_argument('--file', type=str, help='file name')
args = parser.parse_args()

filename = './mynotebooks/second.csv'

def print_file_content(path, file):

    with open(path) as f_obj:
        content = f_obj.readlines()

    if file is not None:

        with open(file, 'w') as file_object:

            for line in content[:20]:
                file_object.write(line)
    
    else:
        for line in content[:20]:
            print(line)

if __name__ == '__main__':
    print_file_content(args.path, args.file)
