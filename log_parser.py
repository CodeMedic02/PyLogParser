# This is the first generator function. It receives the file path and
# opens it in a read-only state. It then strips the /n from each line.
def lines_from_file(path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


# This is the second generator function. It receives its information from
# the lines variable and the pattern variable. This will look at each line
# looking to see if the "pattern" is in the line. If it is, it is yielded.
def matching_lines(lines, pattern):
    for lineItem in lines:
        if pattern in lineItem:
            yield lineItem


# Sample use case using a generated log.txt file.
# This file contains three WARNING lines. When this program is ran
# it should output those three lines.

# Here we are setting up the lines_from_file(file) function.
newLines = lines_from_file(".\\log.txt")

# Here we are setting up the matching_lines(line, pattern) function.
matching = matching_lines(newLines, "WARNING")

# Finally we make use of a for loop to print out the lines which match pattern.
for matchingLine in matching:

    print(matchingLine)
