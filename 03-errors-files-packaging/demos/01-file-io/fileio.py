def read_file(path):
    f = open(path, 'r')  # Generate a readable stream
    output = f.read()  # Read the stream and cache in a variable
    f.close()  # Close the stream
    return output  # Return the output


# print(read_file('./data/one.txt'))


def read_file_with(path):
    with open(path, 'r') as f:  # Generate a readable stream
        output = f.read()  # Read the stream and cache in a variable

    return output  # Return the output


# print(read_file_with('./data/one.txt'))


def write_file_with(path):
    # with open(path, 'w') as f:  # The 'w' mode will overwrite anything in the file with new data
    with open(path, 'a') as f:  # The 'a' mode will append to the preexisting data in the file
        data = f.read()
        words = data.split(' ')
        for word in words:
            ## change all the 'apples' to 'bananas

        f.write(' '.join(words))
        f.write('\nhello world, I was just written to a file')


# write_file_with('./data/one.txt')
# print(read_file_with('./data/one.txt'))

write_file_with('./data/two.txt')
