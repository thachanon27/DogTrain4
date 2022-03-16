from gym.envs.registration import (
    registry,
    register,
    make,
    spec,
    load_env_plugins as _load_env_plugins,
)

# Hook to load plugins from entry points
_load_env_plugins()

# Classic
# ----------------------------------------

register(
    id='dog-v0',
    entry_point='dog_train.envs.basic_env:DogEnv',
)

register(
    id='dog-v2',
    entry_point='dog_train.envs.basic_env:dogEnv2',
)
