from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    #if authenticate then he use get and post
    # it is custom ((((((((((permisssion)))))))))) for user viewswt to only allow user to edit their own profile ,otehrwise ,get and post only
    def has_permission(self,request,view):
        return True
    

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user == obj
        return False
    

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
        # custom permission for (((((((((profileviewset)))))))) to only allow user to edit there own profile.otherwise,get and post.
        def  has_permission(self, request, view):
             return True
        
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True
            
            if not request.user.is_anonymous:
                return request.user.profile == obj
            
            return False