Feature: Verify user search from the Wiki Home Page

  Scenario:
    Given A visitor is on the wikipedia home page
    When  The visitor searches for "furry rabbits"
    Then  A ‘did you mean’ suggestion is displayed
    Then  The visitor can see "20" results

  Scenario:
    Given A visitor is on the search result page for "furry rabbits"
    When  The visitor uses the “Did you mean” feature to correct his search
    When  And select the first entry
    Then  The visitor is on the article page of the first hit
