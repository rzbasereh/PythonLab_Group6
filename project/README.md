# Final Project

To get server you can `build` local docker image with below command or get image from [docker hub](https://hub.docker.com/r/rzbasereh/simple-python-server):

```bash
    $ sudo docker build -t my-simple-server .
```

And to run this container you can use below command:

```bash
    $ sudo docker run -itp3000:3000 -v [images_directory]:/app/images [docker_image_name]
```

Be happy :)
