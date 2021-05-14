from behave import *
from assertpy import assert_that
import creache
import os


@given("{file} exists")
def step_impl(context, file):
    context.known_file = file
    assert_that(os.path.exists(f"./features/sample/{file}.swift")).is_true()


@when("we convert the file")
def step_impl(context):
    creache.run(file=f"./features/sample/{context.known_file}.swift")


@then("it creates a new file named {formatted_file}.swift")
def step_impl(context, formatted_file):
    context.known_file = formatted_file
    assert_that(
        os.path.exists(f"./features/sample/{context.known_file}.swift")
    ).is_true()
