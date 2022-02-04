FROM python:3

COPY pythonserver.py /home/pythonserver.py
CMD ["/home/pythonserver.py"]
ENTRYPOINT ["python3"]

