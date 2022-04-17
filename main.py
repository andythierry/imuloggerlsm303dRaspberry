from datetime import datetime
import time
from lsm303d import LSM303D
import os
lsm = LSM303D(0x1d)  # Change to 0x1e if you have soldered the address jumper

repertoire="LOGS/"+datetime.now().strftime("%d_%m_%Y")
try:
 os.makedirs(repertoire)
except OSError:
 if not os.path.isdir(repertoire):
     raise Exception("Impossible de créer le répertoire de destination")

file=repertoire+'/'+datetime.now().strftime("%d_%m_%Y-%H:%M:%S"+".csv")


fl=open(file, mode='x', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
fl.write("accelerometre X,accelerometre Y,accelerometre Z,")
fl.write("magnetometre X,magnetometre Y,magnetometre Z \n")
while True:
    xyz = lsm.accelerometer()
    mgxyz = lsm.magnetometer()
    print('accelerometre :',xyz)
    print('magnetometre: ',mgxyz)
    #print(("{:+06.2f}g : {:+06.2f}g : {:+06.2f}g").format(*xyz))


    fl.write(("{:+06.2f}g , {:+06.2f}g , {:+06.2f}g").format(*xyz))
    # fl.write("\n")

    fl.write(("{:+06.2f}g , {:+06.2f}g , {:+06.2f}g").format(*mgxyz))
    fl.write('\n')


    time.sleep(0.5)





