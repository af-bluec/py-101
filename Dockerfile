# Multi-Language Sample Project Docker Configuration
# This Dockerfile creates a multi-stage build for efficient containerization

# Stage 1: Build stage for Go application
FROM golang:1.21-alpine AS go-builder

# Install git (required for go modules)
RUN apk add --no-cache git

# Set working directory
WORKDIR /app

# Copy Go source code
COPY server.go .

# Initialize go module and download dependencies
RUN go mod init sample-project && \
    go mod tidy

# Build the Go application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o server server.go

# Stage 2: Build stage for Node.js dependencies
FROM node:18-alpine AS node-builder

# Set working directory
WORKDIR /app

# Copy package files
COPY package.json ./

# Install Node.js dependencies
RUN npm install --production

# Stage 3: Python base setup
FROM python:3.11-alpine AS python-base

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    sqlite \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    pyyaml \
    pytest \
    requests

# Stage 4: Final production image
FROM python:3.11-alpine

# Install runtime dependencies
RUN apk add --no-cache \
    sqlite \
    curl \
    && rm -rf /var/cache/apk/*

# Create non-root user for security
RUN addgroup -g 1001 -S appgroup && \
    adduser -S -D -H -u 1001 -h /app -s /sbin/nologin -G appgroup -g appgroup appuser

# Set working directory
WORKDIR /app

# Copy Python dependencies from python-base stage
COPY --from=python-base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=python-base /usr/local/bin /usr/local/bin

# Copy built Go binary
COPY --from=go-builder /app/server /app/server

# Copy Node.js dependencies
COPY --from=node-builder /app/node_modules /app/node_modules

# Copy application files
COPY main.py utils.js config.yaml ./
COPY test_main.py ./
COPY index.html styles.css ./
COPY database.sql ./
COPY package.json ./

# Create necessary directories
RUN mkdir -p /app/data /app/logs /app/uploads && \
    chown -R appuser:appgroup /app

# Create startup script
RUN cat > /app/start.sh << 'EOF'
#!/bin/sh

echo "Starting Multi-Language Sample Project..."

# Initialize database
echo "Setting up database..."
sqlite3 /app/data/sample.db < /app/database.sql

# Start services
echo "Starting Go server in background..."
/app/server &
GO_PID=$!

echo "Starting Python application..."
python /app/main.py

# Keep Go server running
wait $GO_PID
EOF

RUN chmod +x /app/start.sh && \
    chown appuser:appgroup /app/start.sh

# Switch to non-root user
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Expose ports
EXPOSE 8080 3000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    GO_ENV=production \
    NODE_ENV=production \
    APP_PORT=8080 \
    DATABASE_PATH=/app/data/sample.db

# Volume for persistent data
VOLUME ["/app/data", "/app/logs", "/app/uploads"]

# Labels for metadata
LABEL maintainer="sample-developer@example.com" \
      version="1.0.0" \
      description="Multi-Language Sample Project" \
      org.opencontainers.image.title="Multi-Language Sample Project" \
      org.opencontainers.image.description="A comprehensive sample project demonstrating various programming languages" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.source="https://github.com/example/multi-language-sample-project"

# Default command
CMD ["/app/start.sh"]

# =====================================================
# Build and Run Instructions:
# 
# Build the image:
# docker build -t multi-language-sample .
#
# Run the container:
# docker run -d -p 8080:8080 -p 3000:3000 --name sample-app multi-language-sample
#
# Run with volume mounts for development:
# docker run -d -p 8080:8080 -p 3000:3000 \
#   -v $(pwd)/data:/app/data \
#   -v $(pwd)/logs:/app/logs \
#   --name sample-app multi-language-sample
#
# View logs:
# docker logs sample-app
#
# Execute commands in container:
# docker exec -it sample-app sh
#
# Stop and remove:
# docker stop sample-app && docker rm sample-app
# =====================================================
