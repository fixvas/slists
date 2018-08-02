# Provisioning a new site

## Add non-root user

```bash
adduser username usermod -aG sudo username

ssh-copy-id username@IP_server
```

## Required packages:

* nginx
* Python 3.6
* virtualenv + pip
* Git

eg, on Ubuntu:

```bash
sudo apt-get install nginx

sudo systemctl start nginx

sudo apt install software-properties-common (to get command add-apt-repository)

sudo add-apt-repository ppa:deadsnakes/ppa

sudo apt update

sudo apt-get install git python3.6 python3.6-venv
```

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

username

    └── sites

        └── SITENAME
            ├── database
            ├── source
            ├── static
            └── virtualenv