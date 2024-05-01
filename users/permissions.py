from rest_framework import permissions

class IsUserOwnerGetAndPostOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    return True
  
  def has_object_permission(self, request, view, obj):
    # show only the user's own data
    if request.method in permissions.SAFE_METHODS:
      return True
    # this data is login user's data then he can update it 
    # obj = current user
    if not request.user.is_anonymous:
      # check if the user is the owner of the object
      return request.user == obj
    
    return False