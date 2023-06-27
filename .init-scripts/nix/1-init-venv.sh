#! /bin/bash

venv_dir=~/venv/skc
if [[ -d "$venv_dir" ]];
then
  echo "deleting $venv_dir"
  rm -rf $venv_dir
fi


echo "$venv_dir does not exist, (re)creating ..."
mkdir -p ~/venv/skc
python3 -m venv ~/venv/skc
echo "created venv in $venv_dir"

sudo apt-get -y install \
  build-essential \
  python3-dev \
  libwebkit2gtk-4.0-dev \
  libtiff-dev \
  libnotify-dev \
  freeglut3-dev \
  libsdl1.2-dev \
  libgstreamer-plugins-base1.0-dev

echo
echo "run the following to activate the venv"
echo "source $venv_dir/bin/activate"
