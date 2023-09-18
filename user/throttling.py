
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class Anon5ForMinute(AnonRateThrottle):
    scope = '5_for_min'
    
class User5ForMinute(UserRateThrottle):
    scope = '5_for_min'
    
