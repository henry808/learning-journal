Feature: Permalink
    Implement a way to go to detailed page of an entry with a link

    Scenario: Click permalink button
        Given any user and homepage
        When I click a permalink button
        Then I get redirected to detailed page