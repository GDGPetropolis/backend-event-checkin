FROM python:3.7

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install git+https://github.com/GDGPetropolis/event-certificate-gen.git --upgrade

COPY . .

ENTRYPOINT ["python"]
CMD ["app.py"]