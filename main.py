from flask import Flask
import os

import docker
import schedule
import time

def read_config():
    with open("config/settings.json", "r") as f:
        data = f.read()
        print("Config:", data)

if __name__ == "__main__":
    read_config()

