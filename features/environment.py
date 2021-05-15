from behave import use_fixture, fixture
import os


@fixture
def cleanup(context, timeout=30, **kwargs):
    yield True
    os.remove(f"./features/sample/{context.known_file}.swift")


def before_tag(context, tag):
    if tag == "fixture.cleanup":
        use_fixture(cleanup, context)
