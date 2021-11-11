FROM python:3.9.8-alpine3.14

# Make directory for application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy our source code
COPY /app .

# Run the program
CMD [ "python", "./Tic-Tac-Toe.py" ]