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
        --name python \
        python:3.8.5-alpine3.12 \
        python ${@:2}
else
    docker run \
        -v $PWD:/tmp/working \
        -w=/tmp/working \
        --rm \
        -it \
        --name python \
        python:3.8.5-alpine3.12 \
        $@
fi
