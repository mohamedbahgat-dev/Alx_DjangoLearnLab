from django import forms
from django.core.validators import MinLengthValidator, RegexValidator


# It's best practice to use a dedicated library like nh3 (Ammonia)
# or the older bleach for sanitizing user-submitted HTML to
# prevent XSS. nh3 is a modern, faster alternative to bleach.
# To use, install the library: pip install nh3

class FormExample(forms.Form):
    """
    A secure example form demonstrating key security practices.
    """
    # CharField with max_length to prevent excessively long input.
    # Using a password field is crucial for sensitive data like passwords.
    username = forms.CharField(
        label="Username",
        max_length=150,
        validators=[MinLengthValidator(4)],
        widget=forms.TextInput(attrs={'autocomplete': 'username'}),
    )
    password = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'}),
    )
    # This field accepts user input containing basic HTML tags.
    # It requires explicit sanitization in the clean method.
    user_bio = forms.CharField(
        label="Biography",
        widget=forms.Textarea,
        required=False
    )
    # A regular expression validator for a phone number field
    phone_number = forms.CharField(
        label="Phone Number",
        max_length=15,
        required=False,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    def clean_username(self):
        """
        Custom cleaning for the username field.
        Django's forms automatically handle basic string cleaning and type conversion.
        """
        username = self.cleaned_data.get('username')
        # Here, you might add checks to ensure the username isn't a reserved keyword
        # or that it doesn't already exist in your database.
        return username

    def clean_password(self):
        """
        Custom cleaning for the password field.
        Note: Django's authentication system handles password hashing, so
        never do it here in the form.
        """
        password = self.cleaned_data.get('password')
        # Password complexity validation is handled by validators and Django's
        # authentication system. You can add more complex rules if necessary.
        return password

    def clean_user_bio(self):
        """
        Sanitizes the user_bio field to prevent Cross-Site Scripting (XSS).
        By default, Django's template system provides excellent XSS protection,
        but you should still sanitize user-provided HTML content before saving
        it to the database.
        """
        user_bio = self.cleaned_data.get('user_bio')
        if user_bio:
            # Use nh3 to sanitize the HTML. We define a limited list of
            # allowed tags, attributes, and styles to prevent malicious
            # injections while preserving safe formatting.
            clean_bio = nh3.clean(
                user_bio,
                tags={'b', 'i', 'strong', 'em', 'p', 'br', 'a'},
                attributes={'a': ['href', 'title', 'target']},
                link_rel="noopener noreferrer" # Adds security attributes to links
            )
            return clean_bio
        return user_bio

    def clean(self):
        """
        Custom form-level validation for cross-field checks.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        username = cleaned_data.get("username")

        if password and username and password.lower() in username.lower():
            # Example of a cross-field validation rule.
            self.add_error(
                'password', "Your password cannot contain your username."
            )

        # The cleaned_data dictionary contains all valid, cleaned data.
        return cleaned_data
