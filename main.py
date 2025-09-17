# from vistas.Shell import Shell
from vistas.Shell import Shell
from vistas.shell_prompt import Shell as ShellPromt
from vistas.shell_rich import Shell as shellRich
import asyncio
if __name__ == "__main__":
    shell=ShellPromt( )
    asyncio.run(shell.terminal( ))
