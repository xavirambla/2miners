#!/usr/bin/python
# -*- coding: UTF-8 -*-
import getopt
import sys

import requests
from io import StringIO
import json
import datetime
import time
import subprocess
import random
import os
import signal

"""
class Two_miners:

    def load(self, url):
        self.lastProcess= 0
        content = requests.post(url)
        self.data = content.text
        #data_temp = StringIO(self.data)
        self.dataJSON = json.loads(content.text)
        print(self.dataJSON["currentHashrate"])


#        print(self.dataJSON)

    def save(self, filename):
        actual_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        with open(filename, 'w') as json_file:
            json.dump(self.dataJSON, json_file)

    def init_batch(self,batchs):
        self.num_checks = 0
        batch_exe = batchs[self.lastBatch]
        filename_exe = batchs[self.lastBatch]['filename']


#        process = subprocess.call("taskkill /F /im calc.exe")

#        {'name': "garage_exp_console",               'filename': "Expanse-2miners -Garage.bat"},
        if (self.lastProcess):
            os.killpg(self.lastProcess.pid, signal.SIGTERM)

        os.system("taskkill /F /im "+batch_exe['name'])
        ruta_completa= r'C:/xavi/topcoder/gminer/'+filename_exe
        ruta_completa= filename_exe
        ruta_completa = "calculadora"
        ruta_completa = r'C:/xavi/topcoder/gminer/' + 'calculadora'
        print("ruta {0}".format(ruta_completa))
#        p = subprocess.Popen("C:\Windows\System32\cmd.exe /c "+ruta_completa, creationflags=subprocess.CREATE_NEW_CONSOLE)
#        p = subprocess.Popen("C:/Windows/System32/cmd.exe /c "+ruta_completa, creationflags=subprocess.CREATE_NEW_CONSOLE)
#        p = subprocess.Popen("cmd.exe /c "+ruta_completa, creationflags=subprocess.CREATE_NEW_CONSOLE)
#        p = subprocess.Popen("cmd.exe '"+ruta_completa+".bat'", creationflags=subprocess.CREATE_NEW_CONSOLE)
        p = subprocess.Popen(ruta_completa+".bat", creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.lastProcess = p
        output, errors = p.communicate(input= ruta_completa+".bat")
        print("process  {0}".format(p))
        print(output)
        print(errors)
#        os.system("C:\Windows\System32\cmd.exe /c "+ruta_completa)
#        process= subprocess.call([ruta_completa])
        #process = subprocess.call("taskkill /F /im calc.exe")
     #   print("process :{0}".format(process))


    def run(self,url, title, limites,batchs):
        print("execute")
        miner.load(url)
        self.num_checks = 0   #número de comprobaciones realizadas
        count= 0
        lastdatetime=0
        self.lastBatch=2

        starttime = time.time()
        while count<2:
            time.sleep(6.0 - ((time.time() - starttime) % 6.0))
            self.load(url)

            action = self.check(limites)
            self.init_batch(batchs)
            if (action):
                print("Action : {0}".format(action))
                if action=="restart":
                    self.init_batch(batchs)


            count=count+1




    def check(self, limites):
        action=""

        currentHashrate = self.dataJSON["currentHashrate"]
        for limit in limites:

            if currentHashrate < limit['limit']:
                self.num_checks = self.num_checks+1
                if limit['checks'] < self.num_checks:
                    return limit['action']

        return action

                  

#            count=count+1
#        currentHashrate = self.dataJSON["currentHashrate"]
##        if currentHashrate < minimo_hash:
 #           print("reiniciar")


 #   miner.load(url,2000000)
 #   miner.save("hist/20210501.json")

        


if __name__ == "__main__":
    #define los limites que provocaran el reinicio del sistema
    limites =[
            {
             "description": "To slowly",
             "limit": 2000000,
             "checks":3,
             "action":"restart",
            },
        {
            "description": "not run",
            "limit": 2000,
            "checks": 2,
            "action": "restart",
        },

    ]
    batchs = [
        {'name':"chaby1_exp_console",      'filename': "Expanse-2miners - console-chaby.bat"},
        {'name': "optimizado_exp_console", 'filename': "Expanse-2miners - optimizado - console.bat"},
        {'name': "garage_exp_console",               'filename': "Expanse-2miners -Garage.bat"},

    ]
    miner = Two_miners()

    url = "https://exp.2miners.com/api/accounts/0xe9ff90b3586ec035335819bbf4422b3adb8d004d"

    miner.run(url, "expanse", limites,batchs)
"""

class Two_miners:

    def load(self, url):

        try:
            self.content = requests.post(url)
        except:
            print("Conexión fallida a internet")
            time.sleep(5)
            self.content = requests.post(url)
        self.data = self.content.text
#        print(url)
        #data_temp = StringIO(self.data)
        #        print(self.data)
        #print("----------------------------------")
        try:
            self.dataJSON = json.loads(self.content.text)
            self.hasJSON=True
        except:
            print("NO JSON - {0} ".format(url))
            self.dataJSON={}
            self.hasJSON=False

    ...
    print("Oops!  That was no valid number.  Try again...")


    def is_running(self):
        action=""

        currentHashrate = self.get_currentHashrate()
#        return  currentHashrate > 13700000 and self.lastProcess
        #return  currentHashrate > 19700000 and self.lastProcess   # creo que resultados peores
#        return  currentHashrate > 21700000 and self.lastProcess   # creo que resultados peores
        #return  currentHashrate > 25000000 and self.lastProcess   # creo que resultados peores
#--byueno
#        return  currentHashrate > 16700000 and self.lastProcess   # último buenoentre 13 y 14ç
        return  currentHashrate  >   self.velocidad_minima_hash and self.lastProcess
#        return currentHashrate > 16700000 and self.lastProcess  no tengo claro si mejora tanto, creo que se queda entre 11 y 12
        #return currentHashrate > 13700000 and self.lastProcess  entre 13 y 14
#        return  currentHashrate > 9700000 and self.lastProcess  entre 12 y 13
       # return  currentHashrate > 4847934 and self.lastProcess   entre 10 y 11
#        return currentHashrate > 1 and self.lastProcess   baja por debajo de 10
#        return  currentHashrate > 3 and self.lastProcess

    def get_currentHashrate(self):
        try:
            return self.dataJSON["currentHashrate"]
        except:
            return 0

    def restart(self, name ,  lista_monedas):
        cambiar_moneda = lista_monedas[self.moneda_idx]['cambiar_moneda']
        moneda_idx_old = self.moneda_idx

        #revisamos si debemos cambiar de moneda, consecuencia de la multitud de errores
        if self.nivel_lentitud > cambiar_moneda:
            print("Cambio moneda {0}   {1}".format(self.nivel_lentitud ,cambiar_moneda))
            self.nivel_lentitud = 0
            while True:

                self.moneda_idx = self.moneda_idx+1
                if self.moneda_idx  >= len(lista_monedas):
                    self.moneda_idx=0

                if lista_monedas[self.moneda_idx]['enabled']:
                    print ("Cambiar a : {0}".format(self.moneda_idx))
                    break

        tiempo            = lista_monedas[self.moneda_idx]['tiempo_restart']
        server_connection = lista_monedas[self.moneda_idx]['server_connection']

        args = server_connection+" -w "+name+" -p x --gpu-report-interval 100  "
        executable = "C:/xavi/topcoder/gminer/t-rex.exe "
        full_line =executable+ args
        actual_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


        print( "{0} : {1}".format( actual_time , name))
        moneda = lista_monedas[self.moneda_idx]
        texto = "{4} : Cambio Moneda: {0} HashMin:{1} Tiempo_revision:{2}  Tiempo Restart:{3}  ".format(  moneda['coin'],  moneda['velocidad_minima_hash'],  moneda['tiempo_revision'] ,tiempo ,  time.strftime("%Y%m%d-%H%M%S"))
        self.save_stadistics(  texto +"\n\r" +self.content.text+"\n\r" )


        #        print("lastProcess {0}".format(self.lastProcess))
        if (self.lastProcess):
            self.lastProcess.kill()
            time.sleep( random.randint(5, 15))
            print("{0} Kill Process: Create {1}    {2}".format(actual_time, name, self.nivel_lentitud))
            self.nivel_lentitud =self.nivel_lentitud +1

#        programa = subprocess.call(full_line, stdout=None, stderr=None, shell=True)
        programa = subprocess.Popen(full_line, creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.lastProcess = programa
        time.sleep(tiempo)
        return moneda_idx_old



    def save_stadistics(self , content):

        timestr = time.strftime("%Y%m%d-%H%M%S")
        if ( self.filename=="" ):
            self.filename = "stadistics/2miners_"+time.strftime("%Y%m%d-%H%M%S")+".json"

        with open(self.filename, "a") as f:
            f.write(content)
        f.close
        f = 0  # a veces no se cierra correctamnete el fichero, así lo aseguramos.

    def run(self, lista_monedas , moneda_a_minar):
        self.moneda_idx=moneda_a_minar
        self.filename = ""
        url                 = lista_monedas[self.moneda_idx]['url']
        tiempo = lista_monedas[self.moneda_idx]['tiempo_revision']
        cambioMoneda_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.nivel_lentitud = 0   #lentitudes detectadas

        print("COIN : {0}      WALLET : {1}".format( lista_monedas[self.moneda_idx]['coin'],  lista_monedas[self.moneda_idx] ['wallet']))
        count = random.randint(5, 9)
        self.lastProcess = 0
        self.velocidad_minima_hash = lista_monedas[self.moneda_idx]['velocidad_minima_hash']
        while True:
            self.load(url)
            actual_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            print("{0} Current HashRate {1}      Count  {2}  Coin: {3} {4}".format( actual_time , int(self.get_currentHashrate())/1000000,count ,lista_monedas[self.moneda_idx]['coin'], cambioMoneda_time))
            self.save_stadistics(self.content.text + "\n\r")
            if not self.is_running():
                self.nivel_lentitud = self.nivel_lentitud + 1
                name = lista_monedas[self.moneda_idx]['worker_name'] + "{0}".format(count)
                moneda_idx1= self.restart(name , lista_monedas)
                if self.moneda_idx != moneda_idx1:
                    cambioMoneda_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    print("COIN : {0}      WALLET : {1}".format(lista_monedas[self.moneda_idx]['coin'], lista_monedas[self.moneda_idx]['wallet']))
                    self.moneda_idx=moneda_idx1
                    url = lista_monedas[self.moneda_idx]['url']
                    tiempo = lista_monedas[self.moneda_idx]['tiempo_revision']
                count = count+1
                if (count>5):
                    count=0
            else:
                self.nivel_lentitud = 0
            time.sleep(tiempo)  # hacemos cualquier cosa mientra tanto

# ------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    miner = Two_miners()
    lista_monedas =[]
    # ------------------------------------------------------------------------------------------------------
    #etherum Classic
    wallet = "0x575efcf87acdf6da0c9ae117c6e5511471007eb9"
    moneda = {"wallet":              wallet,
              "server_connection":   "-a etchash -o stratum+tcp://etc.2miners.com:1010 -u "+wallet,
              "coin":                "EtherumClassic",
              "url":                 "https://etc.2miners.com/api/accounts/"+wallet ,
              "tiempo_revision":     30,
              "tiempo_restart":      60*5,
              "worker_name":         "ethc",
              #              "velocidad_minima_hash": 23700000,  # parecqe que empeora y mucho

              #              "velocidad_minima_hash" :  21700000 ,  #  parece que mejora el resultado del anterior ligeramente

              #              "velocidad_minima_hash": 19700000,  # parece que mejora el resultado del anterior
#                           "velocidad_minima_hash" :  12700000 ,  #  creo el segundo el mejor
                            "velocidad_minima_hash" :  16700000 , #  mientrastanto el mejor
              #"velocidad_minima_hash": 10700000,  # está empeorando y se reinicia demasiado , bajo a 107   14092021
              #              "velocidad_minima_hash": 6700000,
              #                            "velocidad_minima_hash" :  19700000 ,
              "cambiar_moneda":      10,
              "enabled": False,
              }
    lista_monedas.append(moneda)
    # ------------------------------------------------------------------------------------------------------
    # Ravencoin
    wallet = "RA8bNGmkPqzFqUBnYygcrzmnpxbMskrvRp"
    moneda = {"wallet": wallet,
              "server_connection": "-a kawpow -o stratum+tcp://rvn.2miners.com:6060 -u " + wallet,
              "coin": "Ravencoin",
              "url": "https://rvn.2miners.com/api/accounts/" + wallet,
              "tiempo_revision": 30,
              "tiempo_restart": 60 * 5,
              "worker_name": "recs",
              "velocidad_minima_hash": 8000000,  # no revisado
              "cambiar_moneda": 10,
              "enabled": True,
              }
    lista_monedas.append(moneda)

#------------------------------------------------------------------------------------------------------
    # expanse
    wallet = "0xe9ff90b3586ec035335819bbf4422b3adb8d004d"
    moneda = {"wallet":              wallet,
              "server_connection":   "-a ethash -o stratum+tcp://exp.2miners.com:3030 -u "+wallet,
              "coin":                "Expanse",
              "url":                 "https://exp.2miners.com/api/accounts/"+wallet ,
              "tiempo_revision":     30,
              "tiempo_restart":      60 * 5,
              "worker_name":         "recs",
              "velocidad_minima_hash": 36700000,  #no revisado
              "cambiar_moneda":      1,
              "enabled": False,
              }
    lista_monedas.append(moneda)
    # ------------------------------------------------------------------------------------------------------
    # Firo
    wallet = "aHf4ZVThYKzHQQ1GwbV7NHdjHXVHADQuR3"
    moneda = {"wallet": wallet,
              "server_connection": "-a mtp -o stratum+tcp://firo.2miners.com:8181 -u " + wallet,
              "coin": "Firo",
              "url": "https://exp.2miners.com/api/accounts/" + wallet,
              "tiempo_revision": 30,
              "tiempo_restart": 60 * 5,
              "worker_name": "fecs",
              "velocidad_minima_hash": 16700000,  # no revisado
              "cambiar_moneda": 2,
              "enabled": False,
              }

    lista_monedas.append(moneda)
    # ------------------------------------------------------------------------------------------------------

    moneda_a_minar = 1
    miner.run(lista_monedas,moneda_a_minar)

