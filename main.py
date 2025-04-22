from flask import Flask
import os

import docker
import schedule
import time

def greet(user_name):
    return "Hello, " + user_name.upper() + "!"

if __name__ == "__main__":
    user_input = None  # Simulate a broken API or null config
    print(greet(user_input))
