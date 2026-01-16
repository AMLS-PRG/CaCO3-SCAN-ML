#!/bin/bash -l

for folder in 4caco3-Eslam-1 4caco3-Eslam-2 8caco3-Eslam-1 8caco3-Eslam-2
do
	cd $folder/extracted-confs
        if [ -f "pw-caco3-0.in" ];
        then
		max_number=`ls -vl pw-caco3-*.in | tail -n 1 | awk '{print $9}'`
		prefix="pw-caco3-"
		suffix=".in"
		max_number=${max_number#"$prefix"}
		max_number=${max_number%"$suffix"}
		echo $max_number
        else
                echo 0
        fi
	cd ../../
done

