Feature: Manager must track :term:`Order` statistics for current day
  As a manager
  I want to have up-to-date :term:`Order`s statistics
  So that I can do my manage'y thing

  Scenario: new GET :term:`Order` statistics request is received
    Given GET :term:`Order` statistics request
    When it is received
    Then response with :term:`Order` statistics is sent

