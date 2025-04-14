import os

if not os.path.exists("data"):
    os.makedirs("data")

from utils import is_gym_open
from logger import log_gym_data

if is_gym_open():
    log_gym_data()
else:
    print("Gym closed, skipping log.")