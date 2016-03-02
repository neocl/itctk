#!/bin/bash

function link_folder {
	FOLDER_PATH=$1
	SYMLINK_NAME=$2
	if [ ! -d ${SYMLINK_NAME} ]; then
		ln -sv ${FOLDER_PATH} ${SYMLINK_NAME}
	else
		echo "Folder ${SYMLINK_NAME} exists."
	fi
}

function link_file {
	FOLDER_PATH=$1
	SYMLINK_NAME=$2
	if [ ! -f ${SYMLINK_NAME} ]; then
		ln -sv ${FOLDER_PATH} ${SYMLINK_NAME}
	else
		echo "File ${SYMLINK_NAME} exists."
	fi
}

link_file   '../modules/barasa/data/SentiWordNet_3.0.0_20130122.txt' 'data/SentiWordNet_3.0.0_20130122.txt'
link_file   '../modules/barasa/data/wn-msa-all.tab' 'data/wn-msa-all.tab'
link_folder 'modules/barasa/barasa' barasa

git submodule init && git submodule update
