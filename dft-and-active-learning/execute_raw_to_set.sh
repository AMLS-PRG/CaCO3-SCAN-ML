#!/bin/bash -l

for folder in 4caco3-Eslam-1 4caco3-Eslam-2 8caco3-Eslam-1 8caco3-Eslam-2
do
	cd $folder/extracted-confs
        /home/ppiaggi/Programs/della-gpu/Software-deepmd-kit-2.1.3-2/deepmd-kit/data/raw/./raw_to_set.sh 301
	cd ../../
done
