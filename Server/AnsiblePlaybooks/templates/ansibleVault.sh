#!/bin/bash
echo "Use for vaulted files:"
echo ""
echo "Ansible-playbook -i hosts fstab.yml --ask-vault-pass"
echo ""
sleep 2
printf "ansible-vault view fstab\n"
ansible-vault view fstab
