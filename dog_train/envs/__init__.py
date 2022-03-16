from gym.envs.registration import register

register(
    id='dog-v0',
    entry_point='dog_train.envs.basic_env:DogEnv',
)

register(
    id='dog-v2',
    entry_point='dog_train.envs.basic_env:dogEnv2',
)
