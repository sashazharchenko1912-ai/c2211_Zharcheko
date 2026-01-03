import logging

logging.basicConfig(level=logging.INFO)

def simulation():
    logging.info("Simulation started")

    for i in range(3):
        logging.info(f"Step {i + 1}")

    logging.info("Simulation finished")


simulation()
