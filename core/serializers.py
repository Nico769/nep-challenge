from rest_framework import serializers

from .models import Node, Resource, CustomUser


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ("id", "title", "content")
        read_only_fields = ("id",)


class NodeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    resources = ResourceSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Node
        fields = ("id", "title", "children", "resources")
        read_only_fields = ("id",)

    def get_children(self, obj):
        return NodeSerializer(obj.get_children(), many=True).data

    def create(self, validated_data):
        new_node = None

        parent_node_id = self.context.get("parentNodeId")
        if parent_node_id:
            parent_node = Node.objects.get(pk=parent_node_id)
            # TODO change the owner according to the identity of the user hitting the API. For now, let's hardcode it to the `resp` user
            new_node = Node.objects.create(
                title=validated_data["title"], parent=parent_node, owner=CustomUser.objects.get(pk=2)
            )
        else:
            new_node = Node.objects.create(title=validated_data["title"], owner=CustomUser.objects.get(pk=2))
        return new_node
