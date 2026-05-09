from datetime import datetime
import hashlib

def log_event(event):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("audit_log.txt", "a") as file:
        file.write(f"{time} - {event}\n")

def save_game(route):
    with open("save_game.txt", "w") as file:
        file.write(route)

def load_game():
    try:
        with open("save_game.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return None
    
def create_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
