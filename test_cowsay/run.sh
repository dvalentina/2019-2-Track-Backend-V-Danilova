#! /usr/bin/env bash

function main {
  if [ $# -eq 0 ]; then
    /usr/games/fortune | /usr/games/cowsay -f dragon
  else
    echo $@ | /usr/games/cowsay -f tux
  fi
}

main $@
