from behave import *
from assertpy import assert_that
import creache
import os


@given("User.swift exists")
def step_impl(context):
    pass


@when("we convert the file")
def step_impl(context):
    creache.run(file="./features/sample/User.swift")
    pass


@then("it creates a new file")
def step_impl(context):
    assert_that(os.path.exists("./User_Entity.swift")).is_true()
