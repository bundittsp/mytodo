from rest_framework import serializers

from .models import ToDoItem


class ToDoItemSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200)
    priority = serializers.ChoiceField(choices=ToDoItem.TYPES)
    complete_flag = serializers.BooleanField(default=False)
    display_order = serializers.IntegerField(default=99)
    create_date = serializers.ReadOnlyField()

    def create(self, validated_data):
        """
        Create and return a new `ToDoItem` instance, given the validated data.
        """
        return ToDoItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `ToDoItem` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.complete_flag = validated_data.get('complete_flag', instance.complete_flag)
        instance.display_order = validated_data.get('display_order', instance.display_order)
        instance.save()
        return instance
