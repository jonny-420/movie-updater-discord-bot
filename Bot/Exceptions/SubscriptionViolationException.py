""" 
This custom exception is used to handle situations where there is a violation of the subscription rules, This rules include:
    1 - such as a user trying to subscribe to a genre they are already subscribed to.
"""
class SubscriptionViolationException(Exception):
    pass
