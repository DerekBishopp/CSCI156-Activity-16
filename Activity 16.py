__author__ = 'Derek'

class Employee:
    pass

class InvalidSocial(ValueError):
    pass

def hopefully(employee_class):

    try:
        x, y, z = employee_class.ss.split('-')
        if employee_class.ss == '078-05-1120':
            raise InvalidSocial
        if x == '000':
            raise InvalidSocial
        if y == '00':
            raise InvalidSocial
        if z == '0000':
            raise InvalidSocial
        if len(x) == 3 and len(y) == 2 and len(z) == 4:
            pass
        else:
            raise InvalidSocial
        x = int(x)
        if x == 666:
            raise InvalidSocial
        else:
            pass
        if x <= 899:
            pass
        else:
            raise InvalidSocial

    except ValueError:
        raise InvalidSocial

def getsoial(employee_class):
    employee_class.ss = input('#SS: ')
    try:
        hopefully(employee_class)
    except InvalidSocial:
        print('Invalid SS \n')
        getsoial(employee_class)


employee = Employee()
getsoial(employee)
print(employee.ss)