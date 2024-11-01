import subprocess

url = "http://108.30.47.158:8000/api/action"
headers = {"Content-Type": "application/json"}
data = '{"action": "greet", "parameters": {"name": "John"}}'

command = [
    "curl",
    "-X", "POST",
    url,
    "-H", f"Content-Type: {headers['Content-Type']}",
    "-d", data
]

result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)
