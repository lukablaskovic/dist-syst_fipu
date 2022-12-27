FROM python:3.10

# Install dependencies
RUN pip install aiohttp aiosqlite pandas numpy

# Copy the script into the container
COPY M0.py /app/M0.py

# Run the script when the container starts
CMD ["python", "/app/M0.py"]
