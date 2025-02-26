FROM python:3.10

ADD dense_neural_class.py .
ADD utils.py .
ADD model.pkl .
ADD requirementsDigit.txt .
ADD server.py .

EXPOSE 8080

RUN pip install --upgrade pip
RUN pip install -r requirementsDigit.txt

CMD [ "python", "./server.py" ]

