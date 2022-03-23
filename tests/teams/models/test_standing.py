from django.test import TestCase
from django.test import tag

from teams.models.standing import Standing

from tests.teams.factories.team import TeamFactory


class StandingModelTest(TestCase):
    """Standing model tests case."""

    maxDiff = None

    def setUp(self) -> None:
        pass

    @tag("solo")
    def test_get_record(self) -> None:
        """get_record() returns a dictionary with relative standings data."""

        data = {
            "played": 28,
            "won": 17,
            "lost": 8,
            "drawn": 3,
            "points": 59,
            "against": 19,
            "goals_for": 57,
            "goal_difference": 38,
        }

        team = TeamFactory(name="Chelsea")

        standing = Standing.objects.create(
            team=team,
            played=data["played"],
            won=data["won"],
            lost=data["lost"],
            drawn=data["drawn"],
            points=data["points"],
            against=data["against"],
            goals_for=data["goals_for"],
            goal_difference=data["goal_difference"],
        )

        expected = {
            "team": {"id": team.id, "name": team.name},
            "played": 28,
            "won": 17,
            "lost": 8,
            "drawn": 3,
            "points": 59,
            "against": 19,
            "goals_for": 57,
            "goal_difference": 38,
        }

        self.assertEqual(standing.get_record(), expected)
