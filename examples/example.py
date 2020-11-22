import asyncio

import aiojarm

loop = asyncio.get_event_loop()
fingerprints = loop.run_until_complete(
    asyncio.gather(
        aiojarm.scan("www.salesforce.com"),
        aiojarm.scan("www.google.com"),
        aiojarm.scan("www.facebook.com"),
        aiojarm.scan("github.com"),
    )
)
print(fingerprints)
