# Import the notification module from plyer library
# plyer allows cross-platform desktop notifications
from plyer import notification

# Define a function to display desktop notifications
def notify(city, msg):
    """Display weather information as a desktop notification"""

    # Call the notify function from plyer.notification
    notification.notify(
        # Set the title of the notification
        title=f"Weather Update - {city}",
        
        # Set the message content of the notification
        message=msg,
        
        # Duration for which the notification will be displayed (in seconds)
        timeout=5
    )
