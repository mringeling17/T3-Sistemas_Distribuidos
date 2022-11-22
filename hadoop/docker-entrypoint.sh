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

#ARCHIVOS UWU
wikiPath1="data/carpeta1/"
wikiPath2="data/carpeta2/"

for file in $wikiPath1*; do
        echo "Cargando $file en HDFS desde $wikiPath1"
        $HADOOP_HOME/bin/hdfs dfs -put $file input
done

for file in $wikiPath2*; do
        echo "Cargando $file en HDFS desde $wikiPath2"
        $HADOOP_HOME/bin/hdfs dfs -put $file input
done

$HADOOP_HOME/bin/hdfs dfsadmin -safemode leave

$HADOOP_HOME/bin/mapred streaming \
        -D mapred.reduce.tasks=1 \
        -input input \
        -output output \
        -mapper mapper.py \
        -reducer reducer.py \
        -file mapper.py \
        -file reducer.py

$HADOOP_HOME/bin/hdfs dfs -cat output/part-00000

# keep the container running indefinitely
tail -f $HADOOP_HOME/logs/hadoop-*-namenode-*.log