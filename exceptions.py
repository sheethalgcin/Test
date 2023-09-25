print('Hello...')
L= [10,20,30,40,50,60]

try:
    x = int(input('enter the first number'))
    y = int(input('enter the second number'))
    s = int(10)
    s = 10 + 'abc'

 #   import sheetal
    q = x/y
   
    print(L[1])


except ValueError:
    print('I got value error')
    y = int(input('enter the second number'))
except ZeroDivisionError:
    print('I got ZeroDivisionError')
except IndexError:
    print("I got index error")
except TypeError:
    print("I got Type error exception")
except Exception:
    print("I got exception")
else:
    print("i got no exception")
finally:
    print('I do always')

print("end of app")
