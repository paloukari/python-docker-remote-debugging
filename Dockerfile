FROM library/python:2.7

RUN pip install ptvsd==3.0.0
COPY main.py /tmp

CMD ["python2", "/tmp/main.py"]