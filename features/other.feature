Feature: Permalink
    Implement a way to go to detailed page of an entry with a link

    Scenario: Click permalink button
        Given any user and homepage
        When I click a permalink button
        Then I get redirected to detailed page

Feature: MarkDown
    Implement a way to MarkDown an entry to be able to make pretty

    Scenario: MarkDown language is submitted in edit entry or create entry text box
        Given MarkDown tag
        When I click submit
        Then I will see the proper MarkDown behaevior in the journal entry on both home and detail page

Feature: Colorize
    Implement a way to colorize text

    Scenario: Code tag is submitted via text box
        Given text box
        When I write code tag and click submit
        Then I will see colorized code samples on detailed and home page