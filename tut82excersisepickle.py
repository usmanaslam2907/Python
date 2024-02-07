"""
pickle
request module to download the iris dataset
"""

# Regular Expression

import re

from tut8 import mystr

"""
findall:  complete string return
split: list return specific
finditer: used for good regular expression
metacharacters used in regular expression
patt=re.compile(r"\n")
"""
patt=re.compile(r'fass')
patt=re.compile(r'.')
patt=re.compile(r'^Tata')# start with Tata
patt=re.compile(r'inn$') # end with inn
patt=re.compile(r'ai+')
patt=re.compile(r'(ai){2}')
patt=re.compile(r'(ai){1}|t')
patt=re.compile(r'(ai){1}|Flax')
print(patt)

#special Sequence

# harry file im[portant
# like validation
#include questions






matches=patt.finditer(mystr)
for match in matches:
    print(match)
