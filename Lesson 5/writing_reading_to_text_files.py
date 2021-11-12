with open('lesson_5.txt', 'w') as file: # 'w' specifies we open the file in writing mode and it will erase anything previously written in the file

    file.write('Hello friend')

with open('lesson_5.txt', 'r') as f: # 'r' specifies we open the file in reading mode

    print(f.read())

    try:
        f.write('Hello friend')
    except:
        print('Cannot write to file in reading mode.')


dictionary_1 = {'a' : [1,2,3], 'b' : [4,5,6]}

with open('lesson_5_1.txt', 'w') as f:

    for key in dictionary_1.keys():
        f.write(f'{key}')
        for element in dictionary_1[key]:
            f.write(f' {element}')
        f.write('\n')

with open('lesson_5_1.txt', 'r') as file:

    line = file.readline() # set the variable we call line to be the string containing the first line of the file

    while line: # this means while line is set to something the while loop will continue and the while loop will break (stop) if we read the next line and there is nothing there

        # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
        # (space is the default leading character to remove)

        # The split function splits a string into a list where each word of the original string is a list item and the input the split function
        # specifies how the words are separated in the original string (space separated or comma separated etc)

        row = line.strip().split(' ')

        print(row) # prints ['a', '1', '2', '3'] for the first row

        line = file.readline() # go to next line

str_1 = 'a 1 2 3 '
print(str_1.strip()) # prints 'a 1 2 3' ie removes empty spaces at the beginning or the end of the string

str_2 = 'a 1 2 3 '
print(str_2.strip('a')) # prints ' 1 2 3 ' ie replaces the character we put as input with an empty space in the string





