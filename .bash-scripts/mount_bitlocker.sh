#!/bin/bash

# Verifica se o usuário é root
if [ "$EUID" -ne 0 ]; then
  echo "Por favor, execute como root."
  exit
fi

# Configurações
DRIVE="/dev/sdXn"  # Substitua pela partição do seu drive BitLocker
MOUNT_POINT="/mnt/bitlocker"
DISLOCKER_MOUNT="$MOUNT_POINT/dislocker"
MOUNT_DIR="$MOUNT_POINT/mount"

# Função para exibir ajuda
function show_help {
  echo "Uso: $0 -p <senha|chave_de_recuperacao>"
  echo "  -p <senha|chave_de_recuperacao> : Senha ou chave de recuperação do BitLocker"
  exit 1
}

# Verifica se o argumento foi passado
if [ "$#" -ne 2 ]; then
  show_help
fi

# Processa os argumentos
while getopts "p:" opt; do
  case $opt in
    p)
      PASSWORD_OR_KEY=$OPTARG
      ;;
    *)
      show_help
      ;;
  esac
done

# Cria os diretórios de montagem se não existirem
mkdir -p $DISLOCKER_MOUNT
mkdir -p $MOUNT_DIR

# Monta o drive usando dislocker
if [[ $PASSWORD_OR_KEY =~ ^[0-9A-Fa-f]{20,40}$ ]]; then
  # Se for uma chave de recuperação
  dislocker -r -V $DRIVE -p$PASSWORD_OR_KEY -- $DISLOCKER_MOUNT
else
  # Se for uma senha
  dislocker -r -V $DRIVE -u$PASSWORD_OR_KEY -- $DISLOCKER_MOUNT
fi

# Monta o sistema de arquivos
mount -o loop $DISLOCKER_MOUNT/dislocker-file $MOUNT_DIR

echo "Drive montado em $MOUNT_DIR"

# Instruções para desmontar
echo "Para desmontar, use:"
echo "  umount $MOUNT_DIR"
echo "  umount $DISLOCKER_MOUNT"


