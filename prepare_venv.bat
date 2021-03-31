python -m venv venv
call venv\Scripts\activate

python -m pip install --upgrade pip
pip install pyhamcrest
pip install coverage
pip install mock

call deactivate
pause
