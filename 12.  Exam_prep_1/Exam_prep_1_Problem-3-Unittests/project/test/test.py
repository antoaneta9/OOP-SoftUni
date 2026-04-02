from project.soccer_player import SoccerPlayer
from unittest import TestCase, main

class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Testcho", 25, 10, "Barcelona")

    def test_init_success(self):
        self.assertEqual("Testcho", self.player.name)
        self.assertEqual(25, self.player.age)
        self.assertEqual(10, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_name_setter_raises_when_name_too_short(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Ivan", 25, 10, "Barcelona")
        self.assertEqual("Name should be more than 5 symbols!", str(ex.exception))

    def test_age_setter_raises_when_age_below_16(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Testcho", 15, 10, "Barcelona")
        self.assertEqual("Players must be at least 16 years of age!", str(ex.exception))

    def test_goals_setter_sets_zero_when_negative(self):
        player = SoccerPlayer("Testcho", 25, -5, "Barcelona")
        self.assertEqual(0, player.goals)

    def test_team_setter_raises_for_invalid_team(self):
        with self.assertRaises(ValueError) as ex:
            SoccerPlayer("Testcho", 25, 10, "Liverpool")
        self.assertEqual(
            "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!",
            str(ex.exception)
        )

    def test_change_team_returns_invalid_team_name_for_invalid_team(self):
        result = self.player.change_team("Liverpool")
        self.assertEqual("Invalid team name!", result)
        self.assertEqual("Barcelona", self.player.team)

    def test_change_team_successfully_changes_team(self):
        result = self.player.change_team("PSG")
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual("PSG", self.player.team)

    def test_add_new_achievement_adds_achievement_when_missing(self):
        result = self.player.add_new_achievement("Golden ball")

        self.assertEqual(
            "Golden ball has been successfully added to the achievements collection!",
            result
        )
        self.assertEqual({"Golden ball": 1}, self.player.achievements)

    def test_add_new_achievement_increases_count_when_existing(self):
        self.player.add_new_achievement("Golden ball")
        result = self.player.add_new_achievement("Golden ball")

        self.assertEqual(
            "Golden ball has been successfully added to the achievements collection!",
            result
        )
        self.assertEqual({"Golden ball": 2}, self.player.achievements)

    def test_lt_returns_other_player_is_top_scorer_when_other_has_more_goals(self):
        other = SoccerPlayer("Ronaldo", 30, 20, "Real Madrid")
        result = self.player < other

        self.assertEqual(
            "Ronaldo is a top goal scorer! S/he scored more than Testcho.",
            result
        )

    def test_lt_returns_self_is_better_goal_scorer_when_self_has_more_goals(self):
        other = SoccerPlayer("Ronaldo", 30, 5, "Real Madrid")
        result = self.player < other

        self.assertEqual(
            "Testcho is a better goal scorer than Ronaldo.",
            result
        )

    def test_lt_returns_self_is_better_goal_scorer_when_equal_goals(self):
        other = SoccerPlayer("Ronaldo", 30, 10, "Real Madrid")
        result = self.player < other

        self.assertEqual(
            "Testcho is a better goal scorer than Ronaldo.",
            result
        )
if __name__ == '__main__':
    main()