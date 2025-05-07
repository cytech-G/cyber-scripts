import os

def run_nmap(target):
    os.system(f"nmap {target}")

if __name__ == "__main__":
    target = input("Enter target IP: ")
    run_nmap(target)
