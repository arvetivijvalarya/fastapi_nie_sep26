input_number = int(input('Enter a number of your choice: '))

try:
    print('NIE' + input_number)
    print(nie + input_number)
except ValueError as e:
    print("Value error occured")
except TypeError as e:
    print("Type error occured")
except NameError as e:
    print("Name error occured")
except:
    print('Some error occured')
finally:
    print('I am Finally and I always Run')
print('Program continues')