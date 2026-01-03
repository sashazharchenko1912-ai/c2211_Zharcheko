import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def run_simulation(steps=5):
    logger.info("Simulation started")

    for step in range(1, steps + 1):
        value = random.randint(1, 100)
        logger.info(f"Step {step}: generated value = {value}")
        time.sleep(0.5)

    logger.info("Simulation finished")


if __name__ == "__main__":
    run_simulation()
