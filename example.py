from pymap.methods.run_method import Methods
from pymap.includes.config import envs, base_fields
from pymap.interactive.interactive import InteractiveSetup


from_env = envs.__dict__
print(from_env)

if __name__ == "__main__":
    # m = Methods(**from_env)
    i = InteractiveSetup(**from_env)
    i.start()
