#!/bin/bash -l

for folder in 4caco3-Eslam-1 4caco3-Eslam-2 8caco3-Eslam-1 8caco3-Eslam-2
do
	cd $folder/extracted-confs
	max_number=`ls -vl pw-caco3-* | tail -n 1 | awk '{print $9}'`
	prefix="pw-caco3-"
	suffix=".in"
	max_number=${max_number#"$prefix"}
	max_number=${max_number%"$suffix"}
	echo $max_number
	for number in `seq 0 $max_number`
	do
                outfile=pw-caco3-"$number".out
                file=pw-caco3-"$number".in
                sed "s/REPLACE1/$file/g" ../../job-base.sh > job.sh
                sed -i "s/REPLACE2/$outfile/g" job.sh
                sbatch < job.sh
 	        echo $folder $number
	done
	cd ../../
done

