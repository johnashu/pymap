# from pymap.methods.marker_methods import MarkerMethods
from pymap.includes.config import envs, base_fields


from_env = envs.__dict__
print(from_env)


# m.new_validator(datadir="test")
# m.create_account()
# m.get_total_votes_for_eligible_validator()


class RPC:
    pass


class PrintStuff:
    def __init__(self, reset: int = 0, **kw):
        self.reset = reset
        self.print_stars = "*" * 93
        super(PrintStuff, self).__init__()


class MarkerMethods(RPC, PrintStuff):

    base_fields = ("rpcaddr", "rpcport", "keystore", "password")

    def __init__(self, **base_fields: dict) -> None:
        self.set_fields(**base_fields)
        self.base_context = {
            k: v for k, v in base_fields.items() if k in self.base_fields
        }
        print(self.rpcaddr)
        super(MarkerMethods, self).__init__(**base_fields)

    def set_fields(self, **base_fields) -> None:
        for k, v in base_fields.items():
            setattr(self, k, str(v))


class Menu(MarkerMethods):
    def __init__(self, **base_fields: dict) -> None:
        # super().__init__(**base_fields)
        super(Menu, self).__init__(**base_fields)


class InteractiveSetup(Menu):
    def __init__(self, **base_fields: dict) -> None:
        # super().__init__(**base_fields)
        super(InteractiveSetup, self).__init__(**base_fields)

    def f(self):
        print(self.print_stars)


m = InteractiveSetup(**from_env)
print(InteractiveSetup.mro())
m.f()


cmd = ["python", "input_test.py"]

# import signal
# import time
# from subprocess import Popen, PIPE

# sig = signal.SIGTERM

# N=9
# M=5

# countlines=0
# p = Popen(cmd, stderr=PIPE, stdout=PIPE, bufsize=1, universal_newlines=True)

# chunk=[]

# out = p.stdout
# if p.stderr:
#     out = p.stderr

# if p.stderr:
#     print(p.stderr)

# for  err in  p.stderr:
#     countlines+=1
#     print(err)
# for out in p.stdout:
#     print(out)

#     if len(chunk)==N:
#         print(chunk)
#         chunk=[]
#         time.sleep(M)

#     if countlines>100:
#         p.send_signal(sig)
#         break

print("done")


import asyncio
from datetime import datetime

class P:
    proc = None

    async def get_output(self, process, std_in):
        process.stdin.write(std_in)
        await process.stdin.drain()  # flush input buffer

        out = await process.stdout.read()  # program is stuck here
        return out

    async def watch(self, stream, prefix="", std_in: str = ""):
        async for line in stream:
            log.info(f"{prefix}  {line.decode().strip()}")
            
    async def create_process(self, cmd):

        p = await asyncio.create_subprocess_exec(*cmd, stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
        
        return p        
    
    async def run(self, cmd, std_in: str = ""):
        p = await self.create_process(cmd)
        if std_in:
            p.stdin.write(std_in)
        await asyncio.gather(self.watch(p.stdout, 'INFO:'), self.watch(p.stderr, 'ERROR:'))        
        
    async def main(self, cmd, std_in):
        await asyncio.gather(self.run(cmd, std_in))

P = P()
# loop = asyncio.get_event_loop()
# r = loop.run_until_complete(P.run(cmd))
# print(P.proc)
# loop.close()

asyncio.run(P.run(cmd, b'Yo Yo What is this then!!\n'))
