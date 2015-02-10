Feature: Edit Entry
    Implement a way to edit an existing entry

    Scenario: There are buttons on homepage
        Given url is homepage
        When on homepage
        Then I will see buttons

    Scenario: Edit button is clicked from the homepage
        Given authorized user and url is at homepage
        When I click the edit button
        Then I get redirected to edit page

    Scenario: Edit button is clicked from the detail page
        Given authorized user and detail
        When I click the edit button
        Then I get redirected to edit page

    Scenario: Edit button is clicked from the homepage
        Given authorized user and homepage
        When I click the edit button
        Then I get redirected to edit page

    Scenario: Edit page loaded
        Given the edit page
        When I finish loading the edit page
        Then I see the old text in the text box

    Scenario: Finished editing and clicked submit
        Given old text
        When I finish editing the text and click submit
        Then I go back to home page with editted entries shown
