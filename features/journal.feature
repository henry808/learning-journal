Feature: Edit Entry
    Implement a way to edit an existing entry

    Scenario: Edit button is clicked from front page or detail page
        Given the edit button
        When I click the button
        Then I go to an edit page

    Scenario: Edit page loaded
        Given the edit page
        When I finish loading the edit page
        Then I see the old text in the text box

    Scenario: Finished editing and clicked submit
        Given old text
        When I finish editing the text and click submit
        Then I go back to home page with editted entries shown

Feature: Permalink
    Implement a way to go to detailed page of an entry with a link

    Scenario: Click permalink button
        Given a permalink button
        When I click the button
        Then I should go to detailed page with url being the permalink

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
