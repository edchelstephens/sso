from factory.faker import Faker

from factory.django import DjangoModelFactory

from teams.models.team import Team


class TeamFactory(DjangoModelFactory):
    """Team factory."""

    name = Faker("name")

    class Meta:
        model = Team
