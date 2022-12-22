#!/bin/bash
sudo service codedeploy-agent start
cd /home/ec2-user/vedat-ex-1
docker-compose up -d --build