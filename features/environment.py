from behave import use_fixture, fixture
import os


@fixture
def cleanup(context, timeout=30, **kwargs):
    print("yike")
    with open("./features/sample/User.swift", "r") as f:
        exists = True
    yield exists

    os.remove("./features/sample/User_Entity.swift")


def before_tag(context, tag):
    if tag == "fixture.cleanup":
        use_fixture(cleanup, context)
