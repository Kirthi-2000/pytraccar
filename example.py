import os
import asyncio
import logging
import aiohttp
from pytraccar import ApiClient

# Set the environment variables
os.environ["TRACCAR_HOST"] = "localhost"
os.environ["TRACCAR_PORT"] = "8082"
os.environ["TRACCAR_USERNAME"] = "admin@gmail.com"
os.environ["TRACCAR_PASSWORD"] = "admin"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)


async def test() -> None:
    """Example usage of pytraccar."""
    async with aiohttp.ClientSession(
        cookie_jar=aiohttp.CookieJar(unsafe=True)
    ) as client_session:
        client = ApiClient(
            host=os.environ["TRACCAR_HOST"],
            port=os.environ.get("TRACCAR_PORT", 8082),
            username=os.environ["TRACCAR_USERNAME"],
            password=os.environ["TRACCAR_PASSWORD"],
            client_session=client_session,
        )
        server = await client.get_server()
        logging.info(
            "Connected to Traccar server (%s:%s) which is running version %s",
            os.environ["TRACCAR_HOST"],
            os.environ.get("TRACCAR_PORT", 8082),
            server["version"],
        )

        # Get a list of all devices
        devices = await client.get_devices()

        # Print device information
        for device in devices:
            print("Device ID:", device.get("id"))
            print("Name:", device.get("name"))
            print("Unique ID:", device.get("uniqueId"))
            print("Status:", device.get("status"))
            print("Position:", device.get("position"))
            print("-----------------------------------------------------")


asyncio.run(test())
