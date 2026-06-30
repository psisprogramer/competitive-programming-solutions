def contraejemplo():
    n = 6
    r = 2
    
    tramos = [
        (2, 1),
        (2, 3),
        (2, 5),
        (5, 4),
        (5, 6)
    ]
    
    
    print(f"{n} {r}")
    
    
    for u, v in tramos:
        print(f"{u} {v}")

if __name__ == '__main__':
    contraejemplo()