import reg_txt
import re

from iteration_utilities import unique_everseen
text = reg_txt.text
l = re.findall('delay\[\d+\]', text)
for i in l:
    n = l.count(i)
    if n > 0:
        print(i, 'количество:', n)