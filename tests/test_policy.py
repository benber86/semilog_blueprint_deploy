import boa
from eth import constants

ZERO_ADDRESS = "0x" + constants.ZERO_ADDRESS.hex()

def test_policy(policy_blueprint, lending_factory):
    with boa.env.prank('0x40907540d8a6C65c637785e8f8B742ae6b0b9968'):
        lending_factory.set_implementations(
            ZERO_ADDRESS, # controller
            ZERO_ADDRESS, # amm
            ZERO_ADDRESS, # vault
            ZERO_ADDRESS, # price oracle
            policy_blueprint,
            ZERO_ADDRESS # gauge
        )

    lending_factory.create(
        '0xf939E0A03FB07F59A73314E73794Be0E57ac1b4E', # borrowed
        '0xFEEf77d3f69374f66429C91d732A244f074bdf74', # collat
        75,
        6000000000000000,
        65000000000000000,
        35000000000000004,
        '0x92473A2fd36EF1d8Ead3251ee1aa08e9568CC10c',
        'test-cvxFXS',
        31709791,
        22196854388
    )
