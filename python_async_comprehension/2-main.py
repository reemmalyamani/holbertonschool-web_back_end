#!/usr/bin/env python3
import asyncio
measure_runtime = __import__('2-measure_runtime').measure_runtime

print(asyncio.run(measure_runtime()))
