FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV RUNNING_IN_DOCKER=true
CMD python -m pytest -s --alluredir=test_results/ /app/tests/ allure serve reports

