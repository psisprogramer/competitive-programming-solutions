import sys
import heapq

def procedimiento():
    idata = sys.stdin.read().split()
    if not idata:
        return
        
    n = int(idata[0])
    k_target = int(idata[1])
    
    a = [0] + [int(x) for x in idata[2:n+2]]
    b = [0] + [int(x) for x in idata[n+2:2*n+2]]
    c = [0] + [int(x) for x in idata[2*n+2:3*n+2]]
    
    def calcularSuperficie(i, j, k):
        x, y, z = a[i], b[j], c[k]
        return 2 * (x * y + y * z + z * x)
    
    heap = []
    visitados = set()
    
    sup_max = calcularSuperficie(n, n, n)
    heapq.heappush(heap, (-sup_max, -n, -n, -n))
    visitados.add((n, n, n))
    
    ans_i, ans_j, ans_k = n, n, n
    
    for _ in range(k_target):
        neg_sup, neg_i, neg_j, neg_k = heapq.heappop(heap)
        ans_i, ans_j, ans_k = -neg_i, -neg_j, -neg_k
        
        if ans_i > 1:
            sig = (ans_i - 1, ans_j, ans_k)
            if sig not in visitados:
                visitados.add(sig)
                s = calcularSuperficie(*sig)
                heapq.heappush(heap, (-s, -sig[0], -sig[1], -sig[2]))
                
        if ans_j > 1:
            sig = (ans_i, ans_j - 1, ans_k)
            if sig not in visitados:
                visitados.add(sig)
                s = calcularSuperficie(*sig)
                heapq.heappush(heap, (-s, -sig[0], -sig[1], -sig[2]))
                
        if ans_k > 1:
            sig = (ans_i, ans_j, ans_k - 1)
            if sig not in visitados:
                visitados.add(sig)
                s = calcularSuperficie(*sig)
                heapq.heappush(heap, (-s, -sig[0], -sig[1], -sig[2]))

    print(f"{ans_i} {ans_j} {ans_k}")

if __name__ == '__main__':
    procedimiento()             