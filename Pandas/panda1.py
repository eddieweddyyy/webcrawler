import pandas as pd
import re

raw = pd.read_excel(r'C:\Users\CKIRUser\Desktop\coding_eddie\Pandas\product.xlsx', engine="openpyxl")
print(raw)

# raw['부가세포함'] = raw['판매가'] * 1.1

def mult(x):
    return x * 1.1

raw['부가세포함'] = raw['판매가'].apply(mult)

def categorize(x):
    x = str(x)
    if 'Chair' in x:
        return 'Chair'
    elif 'Table' in x:
        return 'Table'
    elif 'Mirror' in x:
        return 'Mirror'
    elif 'Sofa' in x:
        return 'Sofa'
    else:
        return 'Unknown'

def categorize2(x):
    x = str(x)
    if re.search('Chair', x):
        return 'Chair'
    elif re.search('Table', x):
        return 'Table'
    elif re.search('Mirror', x):
        return 'Mirror'
    elif re.search('Sofa', x):
        return 'Sofa'
    else:
        return 'Unknown'

def categorize3(x):
    x = str(x)
    if re.findall('Sofa|Mirror', x):
        return 'Furniture'
        
def categorize4(x):
    x = str(x)
    if not re.findall('\D'):
        return 'Error'
    else:
        return x
  

raw['카테고리'] = raw['상품목록'].apply(categorize4)     

# raw['카테고리'] = raw['상품목록'].apply(categorize2)

print(raw)