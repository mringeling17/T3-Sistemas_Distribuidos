#!/bin/bash
set -e
sudo service ssh start

if [ ! -d "/tmp/hadoop-hduser/dfs/name" ]; then
        $HADOOP_HOME/bin/hdfs namenode -format && echo "OK : HDFS namenode format operation finished successfully !"
fi

$HADOOP_HOME/sbin/start-dfs.sh

echo "YARNSTART = $YARNSTART"
if [[ -z $YARNSTART || $YARNSTART -ne 0 ]]; then
        echo "running start-yarn.sh"
        $HADOOP_HOME/sbin/start-yarn.sh
fi

#ARCHIVOS UWU
wikiPath1="data/carpeta1/"
wikiPath2="data/carpeta2/"
scriptsPath="data/scripts/"

$HADOOP_HOME/bin/hdfs dfs -mkdir /tmp
$HADOOP_HOME/bin/hdfs dfs -mkdir /users
$HADOOP_HOME/bin/hdfs dfs -mkdir /jars
$HADOOP_HOME/bin/hdfs dfs -mkdir /user
$HADOOP_HOME/bin/hdfs dfs -mkdir /user/hduser
$HADOOP_HOME/bin/hdfs dfs -mkdir input
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /tmp
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /users
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /jars
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser
$HADOOP_HOME/bin/hdfs dfs -chmod 777 input

$HADOOP_HOME/bin/hdfs dfs -copyFromLocal $scriptsPath /user/hduser
$HADOOP_HOME/bin/hdfs dfs -chmod 777 /user/hduser/scripts

for file in $wikiPath1*; do
        echo "Cargando $file en HDFS desde $wikiPath1"
        $HADOOP_HOME/bin/hdfs dfs -put $file input
done

for file in $wikiPath2*; do
        echo "Cargando $file en HDFS desde $wikiPath2"
        $HADOOP_HOME/bin/hdfs dfs -put $file input
done

$HADOOP_HOME/bin/hdfs dfs -ls 

$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave

$HADOOP_HOME/bin/mapred streaming -mapper $HADOOP_HOME/scripts/mapper.py -reducer $HADOOP_HOME/scripts/reducer.py -input input -output output

$HADOOP_HOME/bin/hdfs dfs -cat output/part-00000

# keep the container running indefinitely
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log