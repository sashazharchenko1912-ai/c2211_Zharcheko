import logging

logging.basicConfig(level=logging.INFO)

logging.info("Sims started")

for step in range(3):
    logging.info(f"Sims step {step + 1}")

logging.info("Sims finished")
