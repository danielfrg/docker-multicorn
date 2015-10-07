# Docker container for Multicorn

Docker container for multicorn based on Postgres 9.4 container with conda for python libraries.

`docker pull danielfrg/multicorn`

`docker run -p 5432:5432 -v $(pwd):/src danielfrg/multicorn`

Python libraries in `/src` will be installed.

See examples for more info.
