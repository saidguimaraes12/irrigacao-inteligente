import sys
import numpy as np

leituras = [50]*1000

leituras = np.array(leituras, dtype=np.uint8)

talhao_1 = {
    "nome" : "Talhão 1",
    "area" : "1 Hectare",
    "umidade" : 68
}

print(leituras.nbytes)