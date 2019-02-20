import pytest

from unittest.mock import patch
from app import create_app, config


@pytest.fixture
def app_test():
    app = create_app(config.test_config)
    return app
