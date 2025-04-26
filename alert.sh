#!/bin/bash

MESSAGE="$1"
LOGFILE="/home/kali/Documents/Python_Scripts/Log_Monitoring/suspicious_activity.log"

# Append to log file
echo "$(date): $MESSAGE" >> "$LOGFILE"

# Optional: Show desktop notification (works only with GUI sessions)
if command -v notify-send &> /dev/null; then
    export DISPLAY=:0
    export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"
    notify-send "🚨 Security Alert" "$MESSAGE" || echo "Notify-send failed"
fi

exit 0

