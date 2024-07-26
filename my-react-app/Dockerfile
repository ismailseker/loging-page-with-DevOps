# # my-react-app/Dockerfile

# # Base image
# FROM node:18

# # Set the working directory
# WORKDIR /app

# # Install dependencies
# COPY my-react-app/package.json my-react-app/package-lock.json /app/
# RUN npm install

# # Copy the React app code
# COPY my-react-app /app/

# # Build the React app
# RUN npm run build

# # Install a simple HTTP server to serve the build files
# RUN npm install -g serve

# # Expose the port the app runs on
# EXPOSE 5000

# # Serve the React app
# CMD ["serve", "-s", "build"]
# React uygulaması için Node.js tabanlı bir Docker imajı oluşturuyoruz
FROM node:16

WORKDIR /app

# Gereksinimleri yükleyin
COPY my-react-app/package.json my-react-app/package-lock.json /app/
RUN npm install

# Uygulama kodunuzu kopyalayın
COPY my-react-app /app/

# Uygulamanızı başlatın
CMD ["npm", "start"]
