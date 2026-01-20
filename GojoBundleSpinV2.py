import asyncio
import lib32 

if __name__ == "__main__":
    try:
        asyncio.run(lib32.main())
    except KeyboardInterrupt:
        pass
