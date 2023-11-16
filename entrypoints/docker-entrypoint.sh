#!/bin/bash
set -e

chmod +x ./WebSockets/bin/activate

. ./WebSockets/bin/activate

python ./WebSockets/app/Mod_Server_Forward.py