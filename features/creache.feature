Feature: Generating files

    @fixture.cleanup
    Scenario: Creating User_Entity.swift
        Given User.swift exists
        When we convert the file
        Then it creates a new file