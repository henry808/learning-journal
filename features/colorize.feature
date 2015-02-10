Feature: Colorize
    Implement a way to colorize text

    Scenario: Code tag is submitted via text box
        Given text box
        When I write code tag and click submit
        Then I will see colorized code samples on detailed and home page