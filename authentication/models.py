from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
import uuid
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Default User Fields Django
# Django -> User --> Firstname, Lastname, Email, Username, Password


def check_value_number(value):
    if len(str(value)) != 16:
        raise ValidationError(
            "Karta raqami 16ta bo'lishiligi kerak"
        )

def check_value_cvv(value):
    if len(str(value)) != 3:
        raise ValidationError(
            "Karta raqami 16ta bo'lishiligi kerak"
        )
        
        

class UserManager(BaseUserManager):
    """
    User yaratish custom fields
    username: bunda username olib tashlanadi
    email: Email login uchun kerak
    password: hamma userlar uchun password field(default holatida bo'ladi)
    phone number: hamme userlar uchun saytdan login qilishda telefon raqam ishlatadi
    """

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email address or email should be valid")

        user = self.model(email=self.normalize_email(email), password=password)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):

        user = self.create_user(email=email, password=password)

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    _unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, unique=True, null=True, blank=True)
    fullName = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        if hasattr(self, "fullName") and hasattr(self, "email"):
            return "%s (%s)" % (self.fullName, self.email)
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class AccountCard(models.Model):
    """
    Foydalanuvchining shaxsiy kartasi
    1.karta nomi -- CharField()
    2.karta raqami -- IntegerField()
    3.karta tugash muddati -- CharField()
    4.cvv - IntegerField()
    """
    _id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="Karta egasi User")
    name = models.CharField(max_length=100, help_text="Karta egasi ism familiyasini kiritishingiz kerak")
    number = models.IntegerField(validators=[check_value_number], help_text="Karta raqamini kiritishingiz kerak. (Etibor bering 16ta dan katta va kichik bo'lmasin)")
    expiry_date = models.CharField(max_length=5, validators=[
        RegexValidator(
            regex=r"^(0[1-9]|1[0-2])\/[0-9]{2}$",
            message="Expiry date must be in the format MM/YY",
            code="invalid_expiry_date"
        ),
    ], help_text="Karta tugash muddatini kiritishingiz kerak. (Etibor bering MM/YY formatida)")
    cvv = models.IntegerField(validators=[check_value_cvv], help_text="Karta CVV kodini kiritishingiz kerak. (Etibor bering 3ta dan katta va kichik bo'lmasin)")
    
    def __str__(self):
        return "%s %s %s %s" % (self.name, self.number, self.expiry_date, self.cvv)
    
    

# Frontend -->  01/23 --> RegexValidator -->  Backend