def log_events(event):
    with open("audit_log.txt", "a") as file:
        file.write(event + "\n")