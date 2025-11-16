# LibraryProject – Permissions and Groups

This app demonstrates role-based access control using Django permissions and groups.

## Custom Permissions

Defined on `bookshelf/models.py`:

```
class Book(models.Model):
    ...
    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]
```

## Views Enforcement

Protected using `@permission_required` in `bookshelf/views.py`:

```
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request): ...

@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request): ...

@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, book_id): ...

@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, book_id): ...
```

## Groups

Use Django Admin (Auth → Groups) to create:

- Viewers: `can_view`
- Editors: `can_view`, `can_create`, `can_edit`
- Admins: `can_view`, `can_create`, `can_edit`, `can_delete` (or use superuser)

Assign users to groups to grant the appropriate permissions.


