#!/bin/bash

ansible-playbook -i hosts -v common.yml --vault-password-file ~/.vault_password
