import requests

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")

# Concert the response objext to a dictionary
response_dict = r.json()

# Process results
print(response_dict.keys())