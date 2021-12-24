FROM python:3

ADD pythonserver.py /home/pythonserver.py
CMD ["/home/pythonserver.py"]
ENTRYPOINT ["python3"]

