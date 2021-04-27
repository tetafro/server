# Description

Ansible playbook to make some settings for Linux server. Nothing important here.

Works only with Ubuntu.

## Run

Install Ansible and copy SSH key to the server.

Set `USER` and `PASSWORD` variables in `.env` file.

Run the playbook
```sh
. .env
ansible-playbook servers.yml \
    -e user="$USER" \
    -e password="$(./passwd.py "$PASSWORD")"
```
