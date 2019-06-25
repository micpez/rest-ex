FROM python:3
ADD get_ratings.py /
ADD config.py /
RUN pip install requests
ENTRYPOINT ["python3", "./get_ratings.py"]
CMD []
