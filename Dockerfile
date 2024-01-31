FROM python:3.11.3-bullseye
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN python -m pip install -U pip && pip install -r src/config/requirements.txt
RUN python -m src.config.scripts.setup_data
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
