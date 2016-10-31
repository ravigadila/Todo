Feature: Testing with lettuce and django

    Scenario: Simple Hello World
        Given I access the url "/add-task/"
        Then I see the header "add task"
