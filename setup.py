#!/bin/python

import sys
import getpass


def main():
    if not getpass.getuser() == "root":
        print("Errore: questo script deve essere eseguito come root")
        return 1
    if len(sys.argv) < 4:
        print("Troppi pochi argomenti, la sintassi deve essere del tipo:")
        print("./setup.py n.cognome password /directory/certificato.crt")
        return 1
    else:
        nmconnection = f"""[connection]
id=Studenti
uuid=
type=wifi

[wifi]
band=bg
mode=infrastructure
ssid=Studenti

[wifi-security]
key-mgmt=wpa-eap

[802-1x]
ca-cert={sys.argv[3]}
domain-suffix-match=unibs.it
eap=peap;
identity={sys.argv[1]}
password={sys.argv[2]}
phase2-auth=mschapv2

[ipv4]
method=auto

[ipv6]
addr-gen-mode=stable-privacy
method=auto

[proxy]
"""
    file = open("/etc/NetworkManager/system-connections/Studenti.nmconnection", "w")
    file.writelines(nmconnection)
    file.close()

if __name__ == "__main__":
        main()
