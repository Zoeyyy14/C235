import requests

for i in range(1,10):
    # URL=f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/profile?id={i}"
    URL=f"https://code.byjusfutureschool.com/s/my-projectsid={i}"
    r=requests.get(url=URL)
    if r.status_code==200:
        print(URL)