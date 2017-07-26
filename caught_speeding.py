speed= 50
is_birthday= True

if speed < 31 or is_birthday and speed < 36:
    print('no ticket')
elif speed > 30 and speed < 51 or speed > 35 and speed < 56 and is_birthday:
    print('small ticket')
else:
    print('big ticket')
    
