FROM python:3.10

# Install dependencies
RUN pip install aiohttp aiosqlite pandas numpy

#Copy the database into container
COPY data.db /app/data.db
# Copy the python script into the container
COPY M0.py /app/M0.py

ENV PYTHONUNBUFFERED=1

# Run the script when the container starts
CMD ["python", "/app/M0.py"]
