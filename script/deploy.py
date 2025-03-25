from src import SemiLogMonetaryPolicy
from moccasin.boa_tools import VyperContract

def deploy() -> VyperContract:
    semilog: VyperContract = SemiLogMonetaryPolicy.deploy_as_blueprint()

def moccasin_main() -> VyperContract:
    return deploy()
