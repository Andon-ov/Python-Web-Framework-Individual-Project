FROM python:3.10

RUN apt update -y && apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

WORKDIR $APP_HOME

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Use the official Python base image with tag 3.10
#FROM python:3.10
#
## Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
#
#ENV HOME=/home/app
#ENV APP_HOME=/home/app/web
#
#WORKDIR $APP_HOME
## Create and set the working directory
##WORKDIR /app
#
## Copy the requirements file
#COPY requirements.txt .
#
## Create and activate a virtual environment
#RUN python -m venv /opt/venv
#ENV PATH="/opt/venv/bin:$PATH"
#
## Upgrade pip and install dependencies
#RUN pip install --no-cache-dir --upgrade pip && \
#    pip install --no-cache-dir -r requirements.txt
#
## Copy the rest of the application files
#COPY . .

# Expose the port (if applicable)
#EXPOSE 8000

# Define the command to run the application
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
