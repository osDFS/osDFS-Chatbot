# Base Images
FROM nginx:1.19.0

# Remove conf file in container
RUN rm /etc/nginx/nginx.conf

# Copy current conf file 
COPY nginx.conf /etc/nginx/

# Remove the current default file 
RUN rm /etc/nginx/conf.d/default.conf

# Put my conf file 
COPY project.conf /etc/nginx/conf.d/