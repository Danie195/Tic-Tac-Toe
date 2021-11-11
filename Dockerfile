FROM python:3.9

ADD Tic-Tac-Toe.py .

RUN pip install pygame

CMD [ "python", "./Tic-Tac-Toe.py" ]