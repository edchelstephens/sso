from django.db import models


class Team(models.Model):
    """Team model."""

    name = models.CharField(max_length=50)

    def __repr__(self) -> str:
        """Team object string representation."""
        return "Team(id={}, name={})".format(self.id, self.name)

    class Meta:
        app_label = "teams"
        db_table = "teams"

    def get_record(self) -> dict:
        """Get team model record."""
        record = {"id": self.id, "name": self.name}

        return record
