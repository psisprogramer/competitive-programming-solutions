import sys
import zlib

def procedimiento():
    idata = sys.stdin.read().split()
    if not idata:
        return
 
    modo = idata[0]
 
    if modo == "compress":
        n = int(idata[1])
        m = int(idata[2])
        nm = n * m
        pixeles_bytes = bytearray(nm * 4)
        idx_byte = 0
        for i in range(3, 3 + nm):
            pixel = idata[i]
            val = int(pixel, 16)
            pixeles_bytes[idx_byte] = (val >> 24) & 0xFF
            pixeles_bytes[idx_byte+1] = (val >> 16) & 0xFF
            pixeles_bytes[idx_byte+2] = (val >> 8) & 0xFF
            pixeles_bytes[idx_byte+3] = val & 0xFF
            idx_byte += 4

        datos_comprimidos = zlib.compress(pixeles_bytes, level=9)
        longitud_bytes = len(datos_comprimidos)
        
        if longitud_bytes >= nm * 4:
            out = [-1]
            for i in range(3, 3 + nm):
                out.append(int(idata[i], 16) & 0xFFFFFFFF)
        else:
            residuo = longitud_bytes % 4
            if residuo > 0:
                datos_comprimidos += b'\x00' * (4 - residuo)
                
            out = [longitud_bytes]
            for i in range(0, len(datos_comprimidos), 4):
                bloque = datos_comprimidos[i:i+4]
                val = int.from_bytes(bloque, byteorder='big')
                out.append(val)
            
        sys.stdout.write(f'{len(out)}\n')
        sys.stdout.write(' '.join(map(str, out)) + '\n')
 
    elif modo == "decompress":
        n = int(idata[1])
        m = int(idata[2])
        k = int(idata[3])
        
        enteros = [int(x) for x in idata[4:4+k]]
        control = enteros[0]
        
        out_lines = []
        if control == -1:
            idx = 1
            for _ in range(n):
                fila = []
                for _ in range(m):
                    fila.append(f"{enteros[idx]:08X}")
                    idx += 1
                out_lines.append(' '.join(fila))
        else:
            datos_comprimidos_recuperados = bytearray()
            for val in enteros[1:]:
                datos_comprimidos_recuperados.extend(val.to_bytes(4, byteorder='big'))
                
            datos_comprimidos_recuperados = datos_comprimidos_recuperados[:control]
            pixeles_bytes = zlib.decompress(datos_comprimidos_recuperados)
            
            indice_byte = 0
            for _ in range(n):
                fila = []
                for _ in range(m):
                    pixel_actual = pixeles_bytes[indice_byte:indice_byte+4]
                    fila.append(pixel_actual.hex().upper())
                    indice_byte += 4
                out_lines.append(' '.join(fila))
                
        sys.stdout.write('\n'.join(out_lines) + '\n')
 
if __name__ == '__main__':
    procedimiento()