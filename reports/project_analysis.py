from datetime import datetime

last_change = datetime.fromisoformat(
    last_status_changed.replace("Z", "")
)

days = (
    datetime.now() - last_change
).days