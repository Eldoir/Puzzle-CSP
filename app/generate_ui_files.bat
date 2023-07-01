@echo off

set PYUIC5_PATH=pyuic5

for %%f in (ui\*.ui) do (
    set FILE_NAME=%%~nf
    %PYUIC5_PATH% -o %%~dpnf.py %%f
)

echo All .ui files processed.