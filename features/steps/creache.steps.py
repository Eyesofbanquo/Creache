from behave import *
import creache
import os


@given("User.swift exists")
def step_impl(context):
    pass


@when("we convert the file")
def step_impl(context):
    creache.run(file="./sample/User.swift")
    pass


@then("it creates a new file")
def step_impl(context):
    assert os.path.exists("./sample/User_Entity.swift")
