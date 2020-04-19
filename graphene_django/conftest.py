import pytest

from graphene_django.settings import graphene_settings

from .registry import reset_global_registry


@pytest.fixture(autouse=True)
def reset_registry_fixture(db):
    yield None
    reset_global_registry()


@pytest.fixture()
def settings():
    settings = dict(graphene_settings.__dict__)
    yield graphene_settings
    graphene_settings.__dict__ = settings
