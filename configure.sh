#!/bin/bash

hostname=$1

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Running configure.sh from ${SCRIPT_DIR}"

case ${hostname} in
    eiger)
        export SPACK_USER_CONFIG_PATH="${SCRIPT_DIR}/config/eiger"
        echo "SPACK_USER_CONFIG_PATH=${SPACK_USER_CONFIG_PATH}"
        ;;
    *)
        echo "${hostname} not supported... =("
        ;;
esac

