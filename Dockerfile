FROM python:3.13-slim
WORKDIR /opt/myapp
COPY /src/ /opt/myapp/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 6789
CMD ["python3", "main.py"]