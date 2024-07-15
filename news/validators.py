from django.core.exceptions import ValidationError


def validate_length_title(value):
    if len(value.split()) < 2:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
