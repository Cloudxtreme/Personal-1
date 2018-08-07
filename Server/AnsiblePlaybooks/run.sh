#!/bin/bash

ansible-playbook -i hosts -v docker.yml --vault-password-file ~/.vault_password
