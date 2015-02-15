Feature: Colorize
    Implement a way to colorize text

    Scenario: Code tag is submitted via text box
        Given an entry with ```X = Y```
        When I go to the detail page with id2
        Then I will see the tag for .codehilite