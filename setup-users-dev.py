from django.contrib.auth import get_user_model

from core.models import Role

User = get_user_model()

# Create `resp` user
resp = User.objects.create_user("resp", "mail@mail.it", "mypwd", role=Role.AvailableRoles.RESPONSABILE)
resp.is_superuser = False
resp.is_staff = False
resp.save()

# Create `op-one` user
op_one = User.objects.create_user("op-one", "mail@mail.it", "mypwd", role=Role.AvailableRoles.OPERATORE)
op_one.is_superuser = False
op_one.is_staff = False
op_one.save()

# Create `op-two` user
op_two = User.objects.create_user("op-two", "mail@mail.it", "mypwd", role=Role.AvailableRoles.OPERATORE)
op_two.is_superuser = False
op_two.is_staff = False
op_two.save()
