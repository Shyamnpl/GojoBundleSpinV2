import asyncio
import libmain 

if __name__ == "__main__":
    try:
        asyncio.run(libmain.main())
    except KeyboardInterrupt:
        pass