Feature: Permalink
    Implement a way to go to detailed page of an entry with a link

    Scenario: See permalink button
        Given the URL
        When I go to the URL or home
        Then I see the permalink button

    Scenario: Click permalink button
        Given any user and homepage
        When I click a permalink button
        Then I get redirected to detailed page
