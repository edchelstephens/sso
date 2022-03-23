from django.db import models


class Team(models.Model):
    """Team model."""

    name = models.CharField(max_length=50)

    class Meta:
        app_label = "teams"
        db_table = "teams"

    def get_record(self) -> dict:
        """Get team model record."""
        record = {"id": self.id, "name": self.name}

        return record
