# init a base image
FROM python:3.10
# define the present working directory
WORKDIR  /app
COPY . /app

RUN pip3 install joblib
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install Flask
RUN pip3 install scikit-learn

CMD ["python", "app.py"]

