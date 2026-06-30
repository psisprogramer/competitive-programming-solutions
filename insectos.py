import sys

def procedimiento():
    inputdata = sys.stdin.read().split()
    
    if not inputdata:
        return

    n = int(inputdata[0])
    
    xmin = xmax = int(inputdata[1])
    ymin = ymax = int(inputdata[2])
    
    for i in range(3, 2 * n + 1, 2):
        x = int(inputdata[i])
        y = int(inputdata[i+1])
        
        if x < xmin: xmin = x
        if x > xmax: xmax = x
        if y < ymin: ymin = y
        if y > ymax: ymax = y
            
    a = xmax - xmin
    b = ymax - ymin
    A = a * b
    

    print(f"{A} {a} {b}")

if __name__ == '__main__':
    procedimiento()