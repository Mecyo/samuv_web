@ECHO OFF
set DIRECTORY="%CD%"
set /p env=Informe um nome para o ambiente virtual e pressione enter:
IF EXIST "%env%""\" (
	goto :ATIVAR
) ELSE (
	goto :CRIAR
)


:VERIFICA
choice /C SN /M "Deseja recriar o banco e o superuser? Pressione: [S]im ou [N]ao"
IF errorlevel=2 goto VERIFICA_MIGRATIONS
IF errorlevel=1 goto CREATEUSER


:VERIFICA_MIGRATIONS
cd "%DIRECTORY%\site"
choice /C SN /M "Deseja realizar os comandos makemigrations e migrate? Pressione: [S]im ou [N]ao"
IF errorlevel=2 goto START
IF errorlevel=1 goto MIGRATES

:MIGRATES
ECHO.
ECHO Executando migrations
ECHO.
ECHO.
python manage.py makemigrations
ECHO Executando migrate
ECHO.
ECHO.
python manage.py migrate
ECHO.
goto START


:CREATEUSER
ECHO Criando superuser
cd "%DIRECTORY%\site"
python manage.py createsuperuser
goto :START

:START
ECHO Iniciando o servidor...
python manage.py runserver
ECHO ON
goto :END
	

:CRIAR
python -m venv "%DIRECTORY%\%env%"
pip install -r "%DIRECTORY%\requirements.txt"
goto :ATIVAR
:ATIVAR
set "VIRTUAL_ENV=%DIRECTORY%\%env%"



if not defined PROMPT (

    set "PROMPT=$P$G"

)



if defined _OLD_VIRTUAL_PROMPT (

    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"

)



if defined _OLD_VIRTUAL_PYTHONHOME (

    set "PYTHONHOME=%_OLD_VIRTUAL_PYTHONHOME%"

)



set "_OLD_VIRTUAL_PROMPT=%PROMPT%"

set "PROMPT=(myenv) %PROMPT%"



if defined PYTHONHOME (

    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"

    set PYTHONHOME=

)



if defined _OLD_VIRTUAL_PATH (

    set "PATH=%_OLD_VIRTUAL_PATH%"

) else (

    set "_OLD_VIRTUAL_PATH=%PATH%"

)



set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

IF EXIST "%env%""\" (
	goto :VERIFICA
) ELSE (
	ECHO Nao foi possivel iniciar o servidor!
)

:END