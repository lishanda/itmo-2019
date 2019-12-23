Feature: Clients must be provided with a menu of :term:`Pizza`
  As a client
  I want to have information about menu
  So that I can view details on each :term:`Pizza`

  Scenario: new GET :term:`Pizza` request is received
    Given GET :term:`Pizza` request
    When it is received
    Then response with :term:`Pizza` list is sent
