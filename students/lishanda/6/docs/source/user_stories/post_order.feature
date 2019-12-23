Feature: Clients must create new :term:`Order`
  As a client
  I want to place :term:`Order`
  So that I can have my pizza to be delivered

  Scenario: new valid :term:`Order` request is received
    Given POST :term:`Order` request
    And :term:`Order` data is valid
    When it is received
    Then create new :term:`Order` in database
    And send notification on customer email

  Scenario: new invalid :term:`Order` request is received
    Given POST :term:`Order` request
    And :term:`Order` data is invalid
    When it is received
    Then no :term:`Order` is created in database
    And response with error code is sent

