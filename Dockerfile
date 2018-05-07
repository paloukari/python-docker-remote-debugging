FROM library/python

RUN pip install ptvsd==3.0.0
COPY main.py /

CMD ["python", "main.py"]