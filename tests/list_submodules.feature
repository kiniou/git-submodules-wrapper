Feature: list submodules

  Scenario: List a single submodule
    Given a git repository "foo"
    And a git repository "subfoo"
    And "subfoo" is a submodule of "foo"
    When I execute "git sm list" in "foo" repository
    Then the submodule "subfoo" must be found in the "git sm list" stdout
      """
      'subfoo' url:../subfoo sha:{submod_sha}
      """
