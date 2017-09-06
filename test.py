import re
line = "rzeng #Richard Zeng richardzeng@scotiabank.com"
line2 = re.match ( r'(.*)\s*#(.*)\s*(.*)\s*(.*@scotiabank.com)', line, re.M|re.I)
print(line2)
