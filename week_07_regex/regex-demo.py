import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern = r"(October|Oct|November|Nov)( \d{1,2}, \d{4})"
    result = result + re.findall(pattern,line)
    return result

def find_name(line):

    pattern = r"M[sr]\.\s[A-Z][a-z]*"
    result = re.findall(pattern,line)

    pattern = r"M[sr]\.[A-Z][a-z]*"
    result = result + re.findall(pattern,line)

    pattern = r"Dr\.\s[A-Z][a-z]*\s[A-Z][a-z]*"
    result = result + re.findall(pattern,line)

    pattern = r"Dr\.\s[A-Z][a-z]*"
    result = result + re.findall(pattern,line)

    return result


#result = find_date("10/15/2023 is a October 13, 2025 date as is 1/23/19")
#print(result)

f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
