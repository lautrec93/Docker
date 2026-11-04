#!/usr/bin/python3
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

print("Content-Type: text/plain; charset=utf-8")
print()
print(f"Efektywny UID: {os.geteuid()}")
print(f"Efektywny GID: {os.getegid()}")
print()

for path in ("/lab-data/ogolny.txt", "/lab-data/poufny.txt"):
    print(f"== {path} ==")
    try:
        with open(path, encoding="utf-8") as f:
            print(f.read().rstrip("\n"))
    except PermissionError as e:
        print(f"Odmowa odczytu: {e.strerror}")
    except OSError as e:
        print(f"Błąd odczytu: {e.strerror}")
    print()
