from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book


class Command(BaseCommand):
    help = "Create default groups (Viewers, Editors, Admins) and assign can_view/can_create/can_edit/can_delete permissions for Book."

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Book)

        perms_map = {
            "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
            "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
            "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
            "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
        }

        viewers, _ = Group.objects.get_or_create(name="Viewers")
        editors, _ = Group.objects.get_or_create(name="Editors")
        admins, _ = Group.objects.get_or_create(name="Admins")

        # Viewers: can_view
        viewers.permissions.set([perms_map["can_view"]])

        # Editors: view, create, edit
        editors.permissions.set([
            perms_map["can_view"],
            perms_map["can_create"],
            perms_map["can_edit"],
        ])

        # Admins: all custom perms on Book
        admins.permissions.set(list(perms_map.values()))

        self.stdout.write(self.style.SUCCESS("Default groups and permissions ensured."))


