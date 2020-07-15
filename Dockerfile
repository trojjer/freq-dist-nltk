FROM python:3.8
RUN useradd --create-home freq_dist
WORKDIR /home/freq_dist
COPY requirements.txt .
RUN pip install -U -r requirements.txt
RUN python -m nltk.downloader stopwords punkt
CMD ["python", "freq_dist.py"]
