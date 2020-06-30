# Base Images 
FROM python:3

# Set the Working Dir  
WORKDIR /usr/src/osDFS/FrontEnd

# Copy the requirement file 
COPY requirements.txt .

# install the packages 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
