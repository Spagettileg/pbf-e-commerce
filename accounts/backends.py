from django.contrib.auth.models import User

class EmailAuth:
    """
    Authenticate a user by an exact match on the email and the password
    """
    def authenticate(self, username=None, password=None):
        """
        Get an instance of 'User' based of the email and verify the password
        """
        
        try:
            user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """
        Used by the Django authentication system to retrieve a user instance
        """
        
        try:
            user = User.objects.get(pk=user_id)  # pk = primary key
            
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
            
            