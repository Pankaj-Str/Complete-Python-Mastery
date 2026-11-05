try:
    name = str(input('Enter Your Name - '))
    age = int(input('Enter Your Age - '))
    height = int(input('Enter Your Height -'))
    print('Your Name is : - ',name)
    print('Your Age is : - ',age)
    print('Your Height is : - ',height)
except ValueError:
    print('Enter Only Number into Age and height')
