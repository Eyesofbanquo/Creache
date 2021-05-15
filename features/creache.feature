Feature: Generating files

    @fixture.cleanup
    Scenario Outline: Creating Files
        Given <file> exists
        When we convert the file
        Then it creates a new file named <formatted_file>.swift


        Examples: Files
            | file        | formatted_file     |
            | User        | User_Entity        |
            | UserUnknown | UserUnknown_Entity |