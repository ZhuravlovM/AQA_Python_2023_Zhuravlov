file1 = open('a.txt', 'r')
lines_that_we_have_read = file1.read()
print(lines_that_we_have_read)
file1.close()

file2 = open('a.txt', 'w')
file2.write('We have written this line of text\n')
file2.writelines(['first line\n', 'second line\n'])
file2.close()

file3 = open('a.txt', 'a')
file3.write('this is a third line of text')
file3.close()

permanent_lines = []
with open('a.txt', 'r') as a:
    permanent_lines = a.readlines()
    print(permanent_lines)

with open('a.txt', 'w') as a:
    for line in permanent_lines:
        if len(line) < 20:
            permanent_lines[permanent_lines.index(line)] = 'We changed this\n'
    a.writelines(permanent_lines)
