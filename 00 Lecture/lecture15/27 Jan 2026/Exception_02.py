try:
    name = str(input('Enter Your Name - '))
    age = int(input('Enter Your Age - '))
    height = int(input('Enter Your Height -'))
    BMI = age/height
    print('Your Name is : - ',name)
    print('Your Age is : - ',age)
    print('Your Height is : - ',height)
    print('BMI = ',BMI)
except ValueError:
    print('Enter Only Number into Age and height')
except ZeroDivisionError:
    print('do not enter zero into height - ')

    try:
        height = int(input('Enter Your Height -'))
        BMI = age/height
        print('Your Name is : - ',name)
        print('Your Age is : - ',age)
        print('Your Height is : - ',height)
        print('BMI = ',BMI)
    except ValueError:
        print('Enter Only Number into Age and height')
    except ZeroDivisionError:
        print('do not enter zero into height - ')
    

    
