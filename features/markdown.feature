Feature: MarkDown
    Implement a way to MarkDown an entry to be able to make pretty

    Scenario: MarkDown language is submitted in edit entry or create entry text box
        Given MarkDown tag
        When I click submit
        Then I will see the proper MarkDown behaevior in the journal entry on both home and detail page