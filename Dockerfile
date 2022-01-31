FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir app/
WORKDIR app/

COPY . app/
RUN pip install --no-cache-dir -r app/requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "app/ai/manage.py", "runserver"]