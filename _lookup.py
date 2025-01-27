import requests

def get_ip_info(ip_address=""):
    url = f"https://ipinfo.io/{ip_address}/json" if ip_address else "https://ipinfo.io/json"
    response = requests.get(url)
    data = response.json()
    
    print(f"IP Address: {data['ip']}")
    print(f"Hostname: {data.get('hostname', 'N/A')}")
    print(f"City: {data.get('city', 'N/A')}")
    print(f"Region: {data.get('region', 'N/A')}")
    print(f"Country: {data.get('country', 'N/A')}")
    print(f"Location: {data.get('loc', 'N/A')}")
    print(f"Org: {data.get('org', 'N/A')}")
    
def main():
    print("Masukkan IP address untuk mencari informasi (atau tekan Enter untuk menggunakan IP publik):")
    ip_address = input()
    get_ip_info(ip_address)

if __name__ == "__main__":
    main()
