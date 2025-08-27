from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, current_year_of_study, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            current_year_of_study=current_year_of_study,
            **extra_fields
        )
        user.set_password(password)  # handles hashing
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, current_year_of_study, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, first_name, last_name, current_year_of_study, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    current_year_of_study = models.IntegerField()
    belongs_to_club = models.ManyToManyField('clubs.Club', blank=True, related_name='members')
    # profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Optional field for profile pictures
    # role_per_club (to identify domain they are part of) (should be many to many in each club) such as ALex is a "Technical" member and "Core" member in the Club A and is "Creative" member in Club B (can be implemented later if needed)

    # Required fields for auth system
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "current_year_of_study"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
