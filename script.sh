sudo docker stop --time=0 $(sudo docker ps -a -q)
sudo docker rm -f $(sudo docker ps -a -q)
sudo docker build  -t sustain . #--no-cache
sudo docker run -d --privileged -p 5000:5000 sustain
sudo docker ps