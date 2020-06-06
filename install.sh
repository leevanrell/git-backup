#!/bin/bash

#fuck pip fuck setuptools fuck python
sudo cp -r git-backup.* /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable git-backup.*
sudo systemctl start git-backup.timer

#jk bbe
sudo pip3 install .