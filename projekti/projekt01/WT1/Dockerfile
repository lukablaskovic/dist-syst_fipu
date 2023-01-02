FROM python:3.10

# Install dependencies
RUN pip install aiohttp

# Copy the python script into the container
COPY WT1.py /app/WT1.py

ENV PYTHONUNBUFFERED=1

# Run the script when the container starts
CMD ["python", "/app/WT1.py"]
