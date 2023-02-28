import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import os
import json
import sys

#RICONTROLLARE: NON FUNZIONA BENE LA CONDIZIONE DI FILTRAGGIO
def fig2(filter_word1):

    directory='C:\\Users\\ASUS\\Desktop\\TESI\\data\\test\\'
    directories=[directory+'noiseless\\',directory+'lima\\', directory+'fakeLima\\']

    for d in directories:

        files = list(os.walk(d))[0][2]
        filtered_files = [file for file in files if (filter_word1) in file]
        print("filtered files: ", filtered_files)
        #importo i dati contenuti dentro al file

        for i in filtered_files:
            filename = d+i
            with open(filename) as fh: #with ti consente di non dovere chiudere manualmente il file alla fine 
                json_string = fh.read()           
                data = json.loads(json_string)
             
            plt.plot(data.keys(), data.values(), 'o--') #label=str(n)+'_'+backendKeyword+str(iter)) 
    
    plt.grid()
    plt.savefig(directory+'figure\\fig2.png',dpi=300)

    return


fig2('1iter')
print('end')