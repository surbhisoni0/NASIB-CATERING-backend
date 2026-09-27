import socket

hosts = [
    "ac-rsuedyw-shard-00-00.1nch5ww.mongodb.net",
    "ac-rsuedyw-shard-00-01.1nch5ww.mongodb.net",
    "ac-rsuedyw-shard-00-02.1nch5ww.mongodb.net",
]

for host in hosts:
    print("=" * 60)
    print("Testing:", host)

    try:
        ip = socket.gethostbyname(host)
        print("DNS:", ip)
    except Exception as e:
        print("DNS ERROR:", type(e).__name__, str(e))
        continue

    try:
        sock = socket.create_connection(
            (host, 27017),
            timeout=10
        )
        print("TCP 27017: CONNECTED")
        sock.close()
    except Exception as e:
        print(
            "TCP 27017 ERROR:",
            type(e).__name__,
            str(e)
        )