# PythonLab_Group6

## Lab 6

### 3-matplotlib

```bash
    $ pip install pandas
    $ python -m pip install -U matplotlib
```

## Final Project

### Install docker:

https://docs.docker.com/get-started/overview/

### Images:

Show installed images:

```bash
    $ sudo docker images
```

Remove specific installed image:

```bash
    $ sudo docker rmi IMAGE
```

> always need to use `sudo` before `docker` command.

### Processes

Show current processes:

```bash
    $ sudo docker ps
```

> with `-a` option we can access to previous processes!

Remove specific EXITED process:

```bash
    $ sudo docker rm CONTAINER_ID
```

Remove all EXITED containers:

```bash
    $ sudo docker container prune
```

sudo docker build --tag my-server .
