import requests

print("\nImportação e uso de um módulo de terceiros:")

url = "https://api.github.com"
response = requests.get(url)
print(f"Status Code da resposta da API do GitHub: {response.status_code}")
