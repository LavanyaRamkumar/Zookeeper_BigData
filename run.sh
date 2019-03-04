#!/bin/bash
zookeeper-3.4.12/bin/zkServer.sh stop
sleep 3
zookeeper-3.4.12/bin/zkServer.sh start
sleep 3
gnome-terminal -e ./single.sh 
gnome-terminal -e ./single.sh 
gnome-terminal -e ./single.sh 
gnome-terminal -e ./single.sh 
gnome-terminal -e ./single.sh

