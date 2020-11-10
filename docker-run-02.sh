#! /usr/bin/env bash

# print the usage and exit
print_usage_and_exit () {
	cat <<____USAGE 1>&2
Usage   : ${0##*/} <var1> <var2> ...
____USAGE
	exit 1
}

# main script starts here

if [ $1 = 'py' ]; then
    docker run \
        -v $PWD:/tmp/working \
        -w=/tmp/working \
        --rm \
        -it \
        --name python-lp \
        gnkm/python-lp:v1 \
        python ${@:2}
elif [ $1 = 'flake' ]; then
    docker run \
        -v $PWD:/tmp/working \
        -w=/tmp/working \
        --rm \
        -it \
        --name python-lp \
        gnkm/python-lp:v1 \
        flake8 ${@:2}
else
    docker run \
        -v $PWD:/tmp/working \
        -w=/tmp/working \
        --rm \
        -it \
        --name python-lp \
        gnkm/python-lp:v1 \
        $@
fi
