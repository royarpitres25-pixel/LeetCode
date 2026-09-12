import paramiko
import getpass
import os

class RemoteFileAccess:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.client = None
        self.sftp = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.hostname, username=self.username, password=self.password)
        self.sftp = self.client.open_sftp()

    def list_dir(self, path):
        return self.sftp.listdir(path)

    def download_file(self, remote_path, local_path):
        self.sftp.get(remote_path, local_path)

    def close(self):
        if self.sftp:
            self.sftp.close()
        if self.client:
            self.client.close()

def main():
    print("Remote File Access CLI")
    host = input("Enter remote IP address: ")
    user = input("Enter username: ")
    pw = getpass.getpass("Enter password: ")
    rfa = RemoteFileAccess(host, user, pw)
    try:
        rfa.connect()
        while True:
            cmd = input("Enter command (ls <dir>, get <remote> <local>, exit): ")
            if cmd.startswith("ls "):
                path = cmd[3:].strip()
                try:
                    files = rfa.list_dir(path)
                    print("\n".join(files))
                except Exception as e:
                    print(f"Error: {e}")
            elif cmd.startswith("get "):
                parts = cmd.split()
                if len(parts) == 3:
                    try:
                        rfa.download_file(parts[1], parts[2])
                        print("Download complete.")
                    except Exception as e:
                        print(f"Error: {e}")
                else:
                    print("Usage: get <remote_path> <local_path>")
            elif cmd == "exit":
                break
            else:
                print("Unknown command.")
    finally:
        rfa.close()

if __name__ == "__main__":
    main()
