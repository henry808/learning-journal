Feature: Edit Entry
    Implement a way to edit an existing entry

    Scenario: Edit page loaded
        Given the edit page and id of 1
        When I finish loading the edit page the url is edit/1
        Then I see the text for id = 1

    Scenario: Finished editing and clicked submit
        Given the first entry of id 1
        When I finish editing the text and click submit
        Then I see the text for id = 1 in homepage
