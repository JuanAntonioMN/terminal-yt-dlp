# from vistas.Shell import Shell
from vistas.Shell import Shell

import asyncio
if __name__ == "__main__":
    shell=Shell( )
    asyncio.run(shell.terminal( ))
