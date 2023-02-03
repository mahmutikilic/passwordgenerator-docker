import random as r
import os as s

PASS_LEN = s.environ.get('PASS_LEN')
PASS_LEVEL = s.environ.get('PASS_LEVEL')
print("Pass Level set:", PASS_LEVEL, "\n Pass Length set:", PASS_LEN)
print("Variable read?: ",'PASS_LEN' in s.environ)
print("Variable read?: ", 'PASS_LEVEL' in s.environ)
PASS_LEN, PASS_LEVEL = int(PASS_LEN), int(PASS_LEVEL)

def save_selection(a,b,c,d):
    if d == 0:
        print("dont save selection")
    if d == 1:
        with open('Savedpass.txt','w') as f:
            f.write(str(a))
        print("{}. password was saved!".format(d))
        #save a to file
    elif d == 2:
        with open('Savedpass.txt','w') as f:
            f.write(str(b))
        print("{}. password was saved!".format(d))
        #save b to file
    elif d == 3:
        with open('Savedpass.txt','w') as f:
            f.write(str(c))
        print("{}. password was saved!".format(d))
        #save c to file

#if not 'PASS_LEN' in s.environ and not 'PASS_LEVEL' in s.environ:
#    print("Global Environment Variables were not found")
#    PASS_LEN , PASS_LEVEL = 8,1

def returnPass(level,length):
    passString = "abcdefghijklmnoprstuvyzwx1234567890ABCDEFGHIJKLMNOPRSTUVYZWX.,!'^+%&/()=?-_"
    if level == 1:
        passresult = "".join(r.sample(passString[:26],length))
        return str(passresult)
    elif level == 2:
        passresult = "".join(r.sample(passString[:36],length))
        return str(passresult)
    elif level == 3:
        passresult = "".join(r.sample(passString[:65],length))
        return str(passresult)
    elif level == 4:
        passresult = "".join(r.sample(passString[:76],length))
        return str(passresult)

print("Hi, Welcome to Password Creator \nYou can see 3 different password examples with ({0}) length and ({1}) difficulty level on the terminal screen. \nWhen run container If you didn't give environment variable, options set to default variable is level = 1 and length = 8.".format(PASS_LEN,PASS_LEVEL))
p1 = returnPass(PASS_LEVEL,PASS_LEN)
p3 = returnPass(PASS_LEVEL,PASS_LEN)
p2 = returnPass(PASS_LEVEL,PASS_LEN)
print("1. password: {0}\n2. password: {1} \n3. password: {2}".format(p1,p2,p3))
sl = int(input("which will you save the password? Exp: 1 (enter) (0 is not saved):"))
save_selection(p1,p2,p3,sl)