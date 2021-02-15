
filename = './mynotebooks/second.csv'

def print_file_content(file):
    with open(filename) as f_obj:
        content = f_obj.readlines()

    for line in content[:20]:
        print(line)

print_file_content(filename)