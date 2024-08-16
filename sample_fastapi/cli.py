import argparse
import asyncio


async def handle_command(args: argparse.Namespace):
    pass


def main():
    parser = argparse.ArgumentParser()
    # TODO: Add some commands

    args = parser.parse_args()

    return asyncio.run(handle_command(args))
