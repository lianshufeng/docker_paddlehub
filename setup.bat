@echo off

:: python3 dist-packages
mkdir cache\python\dist-packages
docker rm -f paddlehub
docker run --name paddlehub -d lianshufeng/paddlehub
docker cp paddlehub:/usr/local/lib/python3.7/dist-packages ./cache/python/
docker rm -f paddlehub

