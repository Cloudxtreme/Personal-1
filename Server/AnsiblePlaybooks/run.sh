#!/bin/bash

ansible-playbook -i hosts -v main.yml --vault-password-file ~/.vault_password
