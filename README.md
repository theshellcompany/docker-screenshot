# docker-screenshot
Dockerized version of chromium to take screenshot of websites. We use this for screenshotting phishing websites. The outputted file has a structured name. The file starts with the ISO-timestamp followed by an underscore and the domain. The outputted file is in png format.



## Building your docker image

```bash
sudo docker build -t screenshot .
```

## Running the container

```bash
mkdir ./output
sudo docker run --rm -v ./output:/output screenshot https://theshell.company
```
