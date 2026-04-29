#!/bin/bash

# Onde está o arquivo ou partição criptografada
VC_VOLUME="/dev/sdd4"    # <-- coloque seu dispositivo ou caminho aqui

# Onde você quer montar
MOUNT_POINT="/tyr"

# Cria o ponto de montagem se não existir
mkdir -p "$MOUNT_POINT"

# Pede a senha do volume com uma janelinha
VC_PASSWORD=$(zenity --password --title="Senha do VeraCrypt")

# Se a pessoa cancelar
if [ $? -ne 0 ]; then
    exit 1
fi

# Pede a senha do usuário (sudo) com uma janelinha
USER_PASSWORD=$(zenity --password --title="Senha do Usuário (sudo)")

if [ $? -ne 0 ]; then
    exit 1
fi

# Usa sudo para montar com veracrypt
echo "$USER_PASSWORD" | sudo -S veracrypt "$VC_VOLUME" "$MOUNT_POINT" --password="$VC_PASSWORD" --pim=0 --protect-hidden=no

# Limpa as variáveis de senha
unset VC_PASSWORD
unset USER_PASSWORD

