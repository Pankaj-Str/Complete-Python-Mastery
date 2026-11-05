#    Set your password :
#    p4n@in
#    Enter your Password : 
#    p4n
#    wrong password ... try 2 more time out of 2
#    p4n@
#    wrong password ... try 1 more time 1
#    p4n@34
#    wrong password ... try 0 more time 0
#    note : user select right password
#    then start MCQ EXAM...

s_pwd = input('Your Set Password - ')
u_pwd = input('Enter Your Password - ')

if s_pwd == u_pwd:
    print("1. Who invented Java Programming  \n 1.  Guido van Rossum \n 2.  James Gosling \n 3.  Dennis Ritchie \n 4.  Bjarne Stroustrup")
    answer0 = int(input('Select Answer  only number - '))
    if answer0 ==  2 :
       print("1. Who invented Java Programming  \n 1.  Guido van Rossum \n 2.  James Gosling \n 3.  Dennis Ritchie \n 4.  Bjarne Stroustrup")
       answer1 = int(input('Select Answer  only number - '))
       if answer1 == 2:
           print('Your Result is pass')
else:
    if s_pwd != u_pwd:
       print('Enter One more time - 2/1')
       u_pwd = input('Enter Your Password - ')