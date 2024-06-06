FROM python:3.10

WORKDIR /app/ 
# 컨테이너에 있는 폴더 이름
COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 80

CMD python main.py
