# # product/validators.py
# from django.core.exceptions import ValidationError
# from datetime import datetime, date
# from rest_framework_simplejwt.authentication import JWTAuthentication

# def moderator_cannot_create(user):
#     if user.is_staff:
#         raise ValidationError("A moderator cannot create objects.")


from django.core.exceptions import ValidationError
from datetime import datetime, date
from rest_framework_simplejwt.authentication import JWTAuthentication

def moderator_cannot_create(user):
    if user.is_staff:
        raise ValidationError("A moderator cannot create objects.")

def validate_user_age_for_product(request_user):

    user = request_user
    if not user:
        raise ValidationError("The user is not authenticated.")

    try:
        token = request_user.auth 
        birthdate_str = token.get('birthdate')
    except AttributeError:
        birthdate_str = None

    if not birthdate_str:
        raise ValidationError("Please specify your birthdate to create a product.")

    birthdate = datetime.fromisoformat(birthdate_str).date()
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if age < 18:
        raise ValidationError("You must be 18 years old to create a product.")