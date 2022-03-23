from django.db import models


class Standing(models.Model):
    """Team standings model."""

    team = models.ForeignKey("Team", on_delete=models.CASCADE, related_name="standings")
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    against = models.IntegerField(default=0)
    goals_for = models.IntegerField(default=0)
    goal_difference = models.IntegerField(default=0)

    class Meta:
        app_label = "teams"
        db_table = "standings"

    def get_record(self) -> dict:
        """Get standings record."""
        record = {
            "team": self.team.get_record(),
            "played": self.played,
            "won": self.won,
            "lost": self.lost,
            "drawn": self.drawn,
            "points": self.points,
            "against": self.against,
            "goals_for": self.goals_for,
            "goal_difference": self.goal_difference,
        }

        return record