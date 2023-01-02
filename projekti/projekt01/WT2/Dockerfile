FROM python:3.10

# Install dependencies
RUN pip install aiohttp

# Copy the script into the container
COPY WT2.py /app/WT2.py

ENV PYTHONUNBUFFERED=1      

# Run the script when the container starts
CMD ["python", "/app/WT2.py"]
