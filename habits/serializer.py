from rest_framework import serializers

from habits.models import Habits
from habits.validators import (
    ChoiceValidator,
    PeriodicityValidator,
    PleasantValidator,
    RelatedPleasantValidator,
    TimeCompleteValidator,
)


class HabitsSerializer(serializers.ModelSerializer):
    validators = [
        TimeCompleteValidator(field="time_to_complete"),
        ChoiceValidator(field1="related_habit", field2="reward"),
        RelatedPleasantValidator(field1="related_habit", field2="is_pleasant_habit"),
        PleasantValidator(
            field1="is_pleasant_habit", field2="reward", field3="related_habit"
        ),
        PeriodicityValidator(field="periodicity"),
    ]

    class Meta:
        model = Habits
        fields = "__all__"
