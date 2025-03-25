import moccasin
import pytest
from src import SemiLogMonetaryPolicy
from boa.contracts.vyper.vyper_contract import VyperContract
from moccasin.config import get_config
from moccasin.moccasin_account import MoccasinAccount


@pytest.fixture
def policy_blueprint() -> VyperContract:
    return SemiLogMonetaryPolicy.deploy_as_blueprint()



@pytest.fixture
def lending_factory() -> VyperContract:
    factory = get_config().get_active_network().manifest_named("lending_factory")
    return factory


@pytest.fixture
def default_account() -> MoccasinAccount:
    return moccasin.config.get_active_network().get_default_account()