import re

user_dict = {}
reg = re.compile(r'[0-9a-zA-Z@_]+.ru')
message_test = 'sana9056@mail.ru'
result = reg.findall(message_test)
need = str(result[0])

suffix = ('.ru', '.com', '.net', '.edu', '')

if need.endswith(suffix):
    if need.find('@') > 0:
        need = need.split('@')
        user_dict['username'] = need[0]
        user_dict['domain'] = need[1]
    else:
        print('Вы ввели некоректную почту')
else:
    print('Вы ввели некоректную почту')

# print(result)
# print(need)
print(user_dict)
