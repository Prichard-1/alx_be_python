def daily_reminder():
    """Function to prompt user for a task and provide a customized reminder"""
    
    # Prompt user for task details with exact required input format
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority using Match Case statement
    match priority:
        case "high":
            reminder = f"⚠️ '{task}' is a high priority task."
        case "medium":
            reminder = f"🔵 '{task}' is a medium priority task."
        case "low":
            reminder = f"🟢 '{task}' is a low priority task."
        case _:
            reminder = f"❓ Unrecognized priority for '{task}'. Please specify 'high', 'medium', or 'low'."

    # Modify reminder if the task is time-sensitive
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    # Print the reminder with required output format
    print("\nReminder:")
    print(reminder)

# Execute the function
daily_reminder()

