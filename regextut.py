#To find out specific pattern from a list


import re
mystr = '''Tata Limited Tata
Dr. David Landsman, executive director
18, Grosvenor Place helloinn
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map 

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243-9727
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
Hai: ha iin ininaiiiaiai kfhksfhkiin
'''

# print(r"\n")  # bina space ke "\n" print karega
# print(r"\n")
#Here r is raw string for example print(r"\n") so we use raw string as a base rule

# findall, search, split, sub, finditer
patt = re.compile(r'fass') #  (re) stands for regular expression. in which we include regular expression. compile vo parameter leta hai jo aap search karengai. it gives number position of the fass which is spanr463 to 467
# patt = re.compile(r'.com')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt= re.compile(r'ai.')
patt=re.compile(r'a.i.')
# patt=re.compile(r'ai*')
# patt=re.compile(r'a*i*')
# patt=re.compile(r'ai+')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')


# Special Sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# # Task
# # Given a string with a lot of indian phone numbers starting from +91
# print(mystr[462:466])
matches = patt.finditer(mystr)
for match in matches:
    print(match)

# print(mystr[150: 152])

"""


"""
