from flask import Flask
import os

import docker
import schedule
import time

def recursive_crash(n):
    return recursive_crash(n + 1)

if __name__ == "__main__":
    recursive_crash(0)
