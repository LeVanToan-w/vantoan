import socket
import threading
import time
from colorama import Fore, Back, Style

HOST = input("Nhập IP của bạn (vd: 127.0.0.1): ").strip()
PORTS = [
    65165, 65239, 61948, 61908
]  # nhiều port

shared_value = {
    "aimlock"
    "aimtrick"
    "aimhead"
    "aimbot"
    "lockhead"
    "FixTrembleHeart"
    "Norecoil"
    "bone_Neck"
    "bone_Head"
}  # giá trị chung

lock = threading.Lock()

# Hàm server cho 1 port
def run_server(port):
    global shared_value
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, port))
        s.listen(1)
        print("Server connected..")
    except Exception as e:
        return

    while True:
        conn, addr = s.accept()
        try:
            data = conn.recv(1024).decode().strip().split()
            response = "Unknown command"

            if len(data) > 0:
                cmd = data[0].upper()

                if cmd == "SET" and len(data) == 3:
                    key, val = data[1], data[2]
                    try:
                        val = int(val)
                    except:
                        pass
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

        except Exception as e:
            conn.sendall(f"Error: {e}".encode())
        finally:
            conn.close()

# Client thực sự set giá trị
def run_client():
    time.sleep(1)  # đợi server khởi động

    # 1. Lấy aimlock từ tất cả port
    for port in PORTS:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET aimlock")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close()
        except:
            print()

        #get aimtrick
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET aimtrick")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()

        # get aimhead
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET aimhead")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()

        # get aimbot
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET aimbot")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()
        
        #get lockhead
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET lockhead")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()
            

        #Get Tremble
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET TrembleHeart")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()

        #Get Recoil
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET Recoil")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()
        
        #bone_Neck
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET bone_Neck")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()

        #bone_Head
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(b"GET bone_Head")
            resp = s.recv(1024).decode()
            print(Fore.GREEN + "Status: Success")
            s.close
        except:
            print()

    # Set value

    #set map train
    #Set aimlock 95
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET aimlock 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #Set aimtrick 90
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET aimtrick 95")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET aimhead 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimbot
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET aimbot 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    #set lockhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET lockhead 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET FixTrembleHeart 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET Norecoil 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET bone_Neck -> bone_Head")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"SET bone_Head -> bone_Neck")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61948))
        s.sendall(b"GETALL")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    # 3. GETALL trên port 8080 để xem giá trị đã thay đổi chưa


    #set map tu chien
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET aimlock 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #Set aimtrick 90
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET aimtrick 95")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET aimhead 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimbot
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET aimbot 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    #set lockhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET lockhead 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET FixTrembleHeart 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET Norecoil 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET bone_Neck -> bone_Head")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"SET bone_Head -> bone_Neck")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61962))
        s.sendall(b"GETALL")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    # 3. GETALL trên port 8080 để xem giá trị đã thay đổi chưa

    #Set map tu chien xep hang
    #Set aimlock 95
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET aimlock 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #Set aimtrick 90
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET aimtrick 95")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET aimhead 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    #set aimbot
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET aimbot 90")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    #set lockhead
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET lockhead 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET FixTrembleHeart 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET Norecoil 100")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET bone_Neck -> bone_Head")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"SET bone_Head -> bone_Neck")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, 61908))
        s.sendall(b"GETALL")
        resp = s.recv(1024).decode()
        print(Fore.GREEN + "Status: Success")
        s.close
    except:
        print()

# Main
if __name__ == "__main__":
    # Tạo server cho nhiều port
    for port in PORTS:
        threading.Thread(target=run_server, args=(port,), daemon=True).start()

    # Chạy client (thật sự SET & GETALL)
    run_client()

    time.sleep(2)