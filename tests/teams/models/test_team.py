from django.test import TestCase

from teams.models.team import Team


class TeamModelTestCase(TestCase):
    """Team model test case."""

    def setUp(self) -> None:
        pass

    def test_get_record_method(self) -> None:
        """get_record() returns a diction containing team name and id."""
        name = "Chelsea"
        team = Team.objects.create(name=name)

        expected = {"id": team.id, "name": team.name}

        self.assertEqual(team.get_record(), expected)
