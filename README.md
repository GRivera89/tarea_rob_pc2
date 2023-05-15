# tarea_rob_pc2
DH y método geométrico del robot KUKA KR 6 R900. Comprobación mediante visualización en RVIZ

## Procedimiento para descargar:
### Ubicarse en la raíz del terminal
$ cd  
$ git clone https://github.com/GRivera89/tarea_rob_pc2.git  
### En la carpeta src dentro de lab_ws descargar el paquete del robot kukakr
$ cd tarea_rob_pc2/lab_ws/src  
$ git clone https://github.com/ros-industrial/kuka_experimental.git  
### Catkin_make a lab_ws
$ cd ..  
$ catkin_make  
### Setear source
En caso descargar los archivos en la raíz del terminal, ejecutar el siguiente comando:  
$ source /home/user/tarea_rob_pc2/lab_ws/devel/setup.bash  
## Simulación en RVIZ
En un terminal ejecutar el siguiente comando:  
$ roslaunch tarea1 display_kr6900sixx.launch  
En otro terminal, ejecutar el codigo correspondiente:
### Testeo del DH
$ rosrun tarea1 test_fkine_dh_kukakr6900sixx
### Testeo del método geométrico
$ rosrun tarea1 test_fkine_kukakr6900sixx
