#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

#define BUFSIZE 1024

void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[]) {
    int sock, port;
    struct sockaddr_in server;
    struct hostent *hp;
    char buffer[BUFSIZE];
    char password_buffer[BUFSIZE];

    if (argc < 2) {
        fprintf(stderr, "Usage: %s hostname [port]\n", argv[0]);
        exit(1);
    }

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) error("Socket creation failed");

    server.sin_family = AF_INET;
    hp = gethostbyname(argv[1]);
    if (hp == NULL) error("Unknown host");

    memcpy(&server.sin_addr, hp->h_addr, hp->h_length);
    port = (argc < 3) ? 80 : atoi(argv[2]);
    server.sin_port = htons(port);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0)
        error("Connecting");

    // Lee datos del servidor
    int n;
    while ((n = read(sock, buffer, BUFSIZE - 1)) > 0) {
        buffer[n] = '\0';
        strcpy(password_buffer, buffer); // ⚠ VULNERABILIDAD: Almacenamiento inseguro
        printf("Received password: %s\n", password_buffer);
    }

    close(sock);
    return 0;
}
