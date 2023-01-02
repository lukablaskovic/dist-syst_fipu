FROM python:3.10

# Install dependencies
RUN pip install aiofiles aiohttp

# Copy the python script into the container
COPY M4.py /app/M4.py

ENV PYTHONUNBUFFERED=1


# Run the script when the container starts
CMD ["python", "/app/M4.py"]
