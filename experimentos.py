import sys

def procedimiento():
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    A = [int(x) for x in data[1:n+1]]
    
    faltantes_indices = [i for i, x in enumerate(A) if x == -1]
    m = len(faltantes_indices)
    
    if m > 0:
        presentes = set(x for x in A if x != -1)
        valores_disponibles = [v for v in range(n + 2) if v not in presentes]
        
        valores_a_insertar = []
        idx_val = 0
        
        while len(valores_a_insertar) < m:
            if idx_val < len(valores_disponibles):
                valores_a_insertar.append(valores_disponibles[idx_val])
                idx_val += 1
            else:
                valores_a_insertar.append(0)
        
        valores_a_insertar.sort()
        
        for i, idx_arr in enumerate(faltantes_indices):
            A[idx_arr] = valores_a_insertar[i]
            
    print(*(A))

if __name__ == '__main__':
    procedimiento()