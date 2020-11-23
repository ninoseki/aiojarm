import asyncio
import os
from typing import List, NamedTuple

import aiometer
import typer

import aiojarm


class Input(NamedTuple):
    hostname: str
    port: int


async def scan(input: Input):
    result = await aiojarm.scan(input.hostname, input.port)
    cols = [str(col) for col in result]
    print(",".join(cols))


def default_max_at_once() -> int:
    return os.cpu_count() or 2


def read_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def is_file_input(hostnames: List[str]) -> bool:
    if len(hostnames) != 1:
        return False

    filename = hostnames[0]
    return os.path.isfile(filename)


def convert_hostnames(hostnames: List[str]) -> List[str]:
    if is_file_input(hostnames):
        filename = hostnames[0]
        return read_from_file(filename)

    return hostnames


async def scan_hosts(hostnames: List[str], port: int, max_at_once: int):
    hostnames = convert_hostnames(hostnames)
    inputs = [Input(hostname, port) for hostname in hostnames]
    await aiometer.run_on_each(scan, inputs, max_at_once=max_at_once)


def main(
    hostnames: List[str] = typer.Argument(
        ..., help="IPs/domains or a file which contains a list of IPs/domains per line"
    ),
    port: int = 443,
    max_at_once: int = default_max_at_once(),
):
    hostnames = convert_hostnames(hostnames)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(scan_hosts(hostnames, port, max_at_once))
    loop.close()


def main_wrapper():
    typer.run(main)


if __name__ == "__main__":
    main_wrapper()
