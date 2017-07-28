from mechanize import Browser
from time import sleep
from pandas import read_csv, DataFrame, to_csv
from lxml import etree
from bs4 import BeautifulSoup
# from sys.stdout import encoding

def get_content(br, code, iter = 1):
    if(iter < 5):
        try:
            br.select_form(nr = 0)
            br.form.find_control(nr = 4).readonly = False
            br.form.set_value(str(code), nr = 4)
            resp = br.submit()
            content = resp.get_data()
            content = BeautifulSoup(content)
            return {'br': br, 'content': content}
        except:
            sleep(1)
            return get_content(br, code, iter = iter+1)
    else:
        return {'br': br, 'content': "Code not found"}

url = "https://www.aapc.com/icd-10/codes/"
br = Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Firefox')]
br.open(url)
icd_codes = read_csv("train.csv")
remaining = set(icd_codes['Event'])
icd_codes = set(icd_codes['Event'])
base_codes = []
codes = []
descriptions = []

for code in icd_codes:
    print code
    dic = get_content(br, code)
    br = dic['br']
    content = dic['content']
    try:
        relevant = content.table.findAll('span')
        l = len(relevant)
        i = 0
        if l>0:
            while i<l:
                #print relevant[i].string.encode(encoding, errors = 'replace'), relevant[i+1].string.encode(encoding, errors = 'replace')
                base_codes.append(code)
                codes.append(relevant[i].string)
                descriptions.append(relevant[i+1].string)
                i = i+2
    except:
        base_codes.append(code)
        codes.append(code)
        descriptions.append("Code not found")
    remaining.remove(code)

fil = open("descriptions.psv", "w")
for i in range(len(descriptions)):
    fil.write(codes[i].encode('utf-8') + "|" + base_codes[i].encode('utf-8') + "|" + descriptions[i].encode('utf-8') + "\n")

fil.close()
