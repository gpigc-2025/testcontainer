import docker
import schedule
import time
import logging

# Configure logging to write to a file
logging.basicConfig(filename='/logs/container_monitoring.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function that checks the current status of all containers, and creates a log file of their statuses
def monitor_containers():
    # Gives this container access to Docker Daemon, so it can view other containers
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    containers = client.containers.list(all=True)
    alert_triggered = False

    for container in containers:
        status = container.status
        if status != 'running':
            alert_triggered = True
            logging.warning(f"ALERT: Container {container.name} is not running (Status: {status})")
            logging.info(f"Logs for {container.name}:")
            # Capture logs and save to the log file
            logs = container.logs().decode('utf-8')
            logging.info(logs)

    if not alert_triggered:
        logging.info("All containers are running smoothly.")

# Schedule the task to run every minute
schedule.every(1).minutes.do(monitor_containers)

if __name__ == "__main__":
    logging.info("Monitoring started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(1)
