FROM python:3.10

# Install dependencies
RUN pip install aiohttp asyncio

# Copy the script into the container
COPY M1.py /app/M1.py

ENV PYTHONUNBUFFERED=1

# Run the script when the container starts
CMD ["python", "/app/M1.py"]
