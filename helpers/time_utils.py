from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+; for older versions, use pytz

def convert_to_eat(iso_date_str):
    """
    Converts an ISO 8601 date string with timezone (e.g., "2025-03-26T17:45:00+00:00")
    to a string formatted in EAT (East Africa Time, 'Africa/Nairobi') as "YYYY-MM-DD HH:MM:SS".
    """
    try:
        # Parse the ISO date string into a datetime object
        dt = datetime.fromisoformat(iso_date_str)
        
        # Convert the datetime to East Africa Time
        dt_eat = dt.astimezone(ZoneInfo('Africa/Nairobi'))
        
        # Return the formatted datetime string
        return dt_eat.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        raise ValueError(f"Invalid ISO date string: {iso_date_str}. Error: {str(e)}")