def to_uppercase(filename):
    with open(filename, 'r') as f:
        content = f.read()
    with open('output.txt', 'w') as f:
        f.write(content.upper())