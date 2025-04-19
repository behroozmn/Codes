import re

# region dot
# (.) -> Note: یک کاراکتر
#     (f.n) --> کاراکتر اول «اِف» و کاراکتر دوم هر چیزی می‌تونه باشه و کاراکتر سوم «اِن» باید باشد
#     (f..n) --> کاراکتر اول «اِف» و کاراکتر دوم و سوم هر چیزی می‌تونه باشه و کاراکتر چهارم «اِن» باید باشد
#
# dot (.)
# text = 'this is fun'
# if re.search('f.n', text):
#     print('this is ok')
#
#
# endregion dot

# region ^

# text = 'Toplearn'
#
# if re.search('^Top', text):
#     print('this is ok')

# endregion

# region $

# text = 'Toplearn'
#
# if re.search('rn$', text):
#     print('this is ok')

# endregion

# region escape

# text = 'this is a book.'
#
# if re.search('book\.', text):
#     print('this is ok')

# endregion

# region set

# text = 'site'
#
# if re.search('si[tdz]e', text):
#     print('this is ok')

# endregion

# region range

# text = 'c'
#
# if re.search('[a-f]', text):
#     print('this is ok')

# endregion

# region exclude

# text = 'siue'
#
# if re.search('si[^tdz]e', text):
#     print('this is ok')

# endregion

# region repeat

# text = '09123456789'
#
# if re.match('[0-9]{11}', text):
#     print('this is ok')

# endregion

# region other characters

# decimal digits => \d
# non decimal digits => \D
# white space => \s
# non white space => \S
# word => \w
# non word => \W

# text = 'abcdef'
# if re.match('(abc|cde)', text):
#     print('this is ok')

# endregion

# region email regex

text = '787jhjkj@test.com'
if re.match('^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$', text):
    print('email is valid')

# endregion
