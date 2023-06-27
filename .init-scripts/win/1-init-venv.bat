@echo off
set venv_dir=%USERPROFILE%\venv\skc
if exist %venv_dir% (
  echo deleting %venv_dir%
  rmdir /s /q %venv_dir%
)

echo %venv_dir% does not exist, (re)creating ...
mkdir %venv_dir%
  
python -m venv %venv_dir%
echo created venv in %venv_dir%

echo run the following to activate the venv
echo %venv_dir%\Scripts\activate
