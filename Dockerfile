FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "semantics.py"]
