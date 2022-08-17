from pymap.methods.run_method import Methods
from pymap.includes.config import envs, base_fields


from_env = envs.__dict__
print(from_env)

m = Methods(**from_env)

m.create_account()
