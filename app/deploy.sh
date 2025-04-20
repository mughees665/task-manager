#!/bin/bash

# Replace these with your actual EC2 info
EC2_USER=ubuntu
EC2_IP="your-ec2-ip"
PEM_FILE="your-key.pem"

# Copy files to EC2
scp -i $PEM_FILE -r * $EC2_USER@$EC2_IP:/home/ubuntu/task-manager

# SSH into EC2 and run setup
ssh -i $PEM_FILE $EC2_USER@$EC2_IP << EOF
    cd task-manager
    chmod +x setup.sh
    ./setup.sh
EOF
