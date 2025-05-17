import re

# Behrooz: regexr.com

names = [
    'data.png', 'memory.txt', 'data.txt', 'image.png', 'momy.png'
]

for item in names:
    if re.search('m.m', item):
        print(item)

# re.search('m.m', item): #اگر در این رشته موجود بود
# re.match('m.m', item): # باید دقیقا این رشته مساوی الگو باشد
