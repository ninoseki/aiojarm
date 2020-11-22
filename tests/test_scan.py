import pytest

import aiojarm


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "hostname,expected",
    [
        (
            "www.salesforce.com",
            "2ad2ad0002ad2ad00042d42d00000069d641f34fe76acdc05c40262f8815e5",
        ),
        (
            "www.facebook.com",
            "27d27d27d29d27d1dc41d43d00041d741011a7be03d7498e0df05581db08a9",
        ),
    ],
)
async def test_scan(hostname: str, expected: str):
    result = await aiojarm.scan(hostname)
    assert result[3] == expected
