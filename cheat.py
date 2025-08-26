import socket
import threading
import time

HOST = "127.0.0.1"
PORTS = [
    63720, 8080, 63721, 63722, 63723, 63724,
    63725, 63726, 63727, 63728, 63729, 35618,
    53317, 35624
]  # nhiều port

shared_value = {
    "aimlock": 95,
    "aimhead": 90,
    "aimbot": 90,
    "fixtremble": 100,
    "fixrecoil": 100
}  # giá trị chung

lock = threading.Lock()


# Hàm server cho 1 port
def run_server(port):
    global shared_value
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    s.listen(1)
    print(f"Server listening on {HOST}:{port}")

    while True:
        conn, addr = s.accept()
        print(f"Connected by {addr} on port {port}")

        data = conn.recv(1024).decode().strip().split()
        response = "Unknown command"

        if len(data) > 0:
            cmd = data[0].upper()

            if cmd == "SET" and len(data) == 3:
                key, val = data[1], data[2]
                with lock:
                    shared_value[key] = val
                response = f"{key} updated to {val}"

            elif cmd == "GET" and len(data) == 2:
                key = data[1]
                with lock:
                    if key in shared_value:
                        response = f"{key} = {shared_value[key]}"
                    else:
                        response = f"{key} not found"

            elif cmd == "GETALL":
                with lock:
                    response = str(shared_value)

        conn.sendall(response.encode())
        conn.close()


# Test client (chạy sau server)
def run_client():
    time.sleep(1)  # đợi server khởi động
    for port in PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, port))
        s.sendall(b"GET aimlock")
        print("Status: ON")
        s.close()

    # Thử SET trên port 63720
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 63720))
    s.sendall(b"SET aimhead 123")
    print("Status: ON")
    s.close()

    # Thử GETALL trên port 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, 8080))
    s.sendall(b"GETALL")
    print("Status: ON")
    s.close()


# Main
if __name__ == "__main__":
    # Tạo server cho nhiều port
    for port in PORTS:
        threading.Thread(target=run_server, args=(port,), daemon=True).start()

    # Chạy client test
    run_client()

    time.sleep(2)