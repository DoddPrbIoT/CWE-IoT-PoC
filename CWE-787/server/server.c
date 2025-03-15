#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 12345
#define BUFFER_SIZE 16  

void process_data(char *data) {
    char buffer[BUFFER_SIZE];
    strcpy(buffer, data);  
    printf("Received data: %s\n", buffer);
}

int main() {
    int sockfd;
    struct sockaddr_in server_addr, client_addr;
    char buffer[1024];  
    socklen_t addr_len = sizeof(client_addr);

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    if (bind(sockfd, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("Binding error");
        exit(EXIT_FAILURE);
    }

    printf("🚀 IoT UDP Server is running on port %d...\n", PORT);
    printf("Waiting for incoming data...\n");

    while (1) {
        int received_bytes = recvfrom(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr*)&client_addr, &addr_len);
        if (received_bytes > 0) {
            buffer[received_bytes] = '\0';  
            process_data(buffer);  
        }
    }

    close(sockfd);
    return 0;
}
