FROM debian:latest

WORKDIR /app

# Install essential tools
RUN apt-get update && apt-get install -y gcc

# Copy source code
COPY server.c .

# Compile the code
RUN gcc server.c -o server -fno-stack-protector -z execstack

# Expose the UDP port
EXPOSE 12345/udp

# Run the server
CMD ["./server"]
