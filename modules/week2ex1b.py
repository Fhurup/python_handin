filename = './mynotebooks/msg.txt'
## thistuple = ("apple", "banana", "cherry", "elefant")

def write_list_to_file(output_file, *lst):
    

    with open(filename, 'w') as file_object:

        for line in lst:
            file_object.write(str(line))

write_list_to_file(filename, ('apple', 'banana', 'cherry', 'elefant'))