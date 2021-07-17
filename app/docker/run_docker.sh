#!/bin/sh

docker run --cidfile ./app/docker/tst.cid  ubuntu && res=`cat ./app/docker/tst.cid` && echo $res