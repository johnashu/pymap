from pymap.methods.run_method import  Methods
from pymap.includes.config import envs

base = envs.__dict__
print(base)

m = Methods(**base)

m.create_account()