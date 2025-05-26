import requests
import tomllib
import re
import os

if __name__ == "__main__":
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    with open("aissurance.toml", "rb") as f:
        config = tomllib.load(f)
    if "PrivateAEYE" in config:
        print(requests.get(f"{config["PrivateAEYE"]["api_url"]}\
/api/crawl/{config["PrivateAEYE"]["project_name"]}\
?url={config["PrivateAEYE"]["check_url"]}"))
        comparison = requests.get(f"{config["PrivateAEYE"]["api_url"]}\
/api/compare_latest/{config["PrivateAEYE"]["project_name"]}")
        print(comparison)
        errors = re.compile(
            r'[0-9]+\. \*\*(?P<title>.+)\*\* \- \*\*Description\*\*: ' +
            r'(?P<description>.+)( \- \*\*Pixel Coordinates\*\*: .+)?')
        observations = comparison.text.split('#### ')
        for observation in observations:
            if observation.startswith('[Error] '):
                observation = observation[8:]
                errs = [e.groupdict() for e in errors.finditer(observation)]
                for err in errs:
                    desc = err["description"].replace('"', "'")
                    if "WikAI" in config:
                        jsonobj = {
                            "projectName": config["WikAI"]["project_name"],
                            "title": err["title"],
                            "description": desc
                        }
                        resp = requests.post(f"{config["WikAI"]["api_url"]}", jsonobj)
                    resp = requests.post(
                        f"https://api.github.com/repos/\
{config["PrivateAEYE"]["project_repo"]}/issues",
                        f"{{\"title\":\"{err["title"]}\",\
\"body\":\"{desc}\"}}",
                        headers={
                            "Accept": "application/vnd.github+json",
                            "Authorization": f"Bearer {GITHUB_TOKEN}",
                            "X-GitHub-Api-Version": "2022-11-28"
                            }
                        )
                    if resp.status_code != 201:
                        print(f"Error creating issue ({err["title"]}): \
{resp.status_code}\n\t{resp.text}")