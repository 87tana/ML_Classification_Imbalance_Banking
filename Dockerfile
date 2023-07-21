# Start your image with a node base image
FROM python:3.10-bookworm

# The /app directory should act as the main application directory
WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Copy local directories to the current local directory of our docker image (/app)

COPY . .


CMD ["python", "./train.py" , "--data", "./bank-full.csv", "--outdir", "./"]