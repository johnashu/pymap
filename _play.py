from pymap.methods.run_method import Methods
from pymap.includes.config import envs, base_fields


from_env = envs.__dict__
print(from_env)

m = Methods(**from_env)

# m.new_validator(datadir="test")
# m.create_account()
m.get_total_votes_for_eligible_validator()
