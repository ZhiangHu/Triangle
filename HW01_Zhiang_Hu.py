class Triangle(object):
    def __init__(self):
        super().__init__()
        
    def triangle(self, a, b, c) :
        if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
            if (a == b) and (a == c):
                print('Equilateral triangle')
                return 3
            elif ((a == b) or (a == c) or (b == c)):
                print('Isosceles triangle')
                return 2
            elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a):
                print('Right triangle')
                if ((a == b) or (a == c) or (b == c)):
                    print('Isosceles right triangle')
                    return 2
                else:
                    return 1
            else:
                print('General triangle')
                return 1
        else:
            print('Not a triangle')
 
if __name__ == '__main__':
    while True:
        a = int(input('Please enter the value of a:'))
        b = int(input('Please enter the value of b:'))
        c = int(input('Please enter the value of c:'))
        if (a > 0 and a <= 200) and (b > 0 and b <= 200) and (c > 0 and c <= 200):
            print('The three sides of the input are correct')
            triangle = Triangle()
            print('The number of equal sides is:', triangle.triangle(a, b, c))
            break
        else:
            print('Wrong input')
