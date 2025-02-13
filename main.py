from flask import Flask
import os

import docker
import schedule
import time

if __name__ == "__main__":
    print("Container is running... will crash in 5 seconds.")
    time.sleep(5)
    raise RuntimeError("Intentional crash for testing purposes.")
