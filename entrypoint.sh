#!/bin/bash

gdown https://drive.google.com/uc?id=1bByEqiC6pr2AfjmV8prp8C2XWq5z5AhK
ansible-playbook ansible/download-model.yml --vault-password-file ./vault-pass.txt
