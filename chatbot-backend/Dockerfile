FROM python:3.9.5-buster

WORKDIR /

COPY . ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -c "import nltk; nltk.download('punkt', download_dir='/usr/local/nltk_data')"
RUN python -m nltk.downloader punkt

CMD ["python", "-u", "api.py"]