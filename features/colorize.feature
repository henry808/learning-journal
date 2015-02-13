Feature: Colorize
    Implement a way to colorize text

    Scenario: Code tag is submitted via text box
        Given an entry with      print('Text')
        When I go to the detail page with id2
        Then I will see the tag for .codehilite