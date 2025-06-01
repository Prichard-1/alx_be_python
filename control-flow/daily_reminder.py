def daily_reminder():
    """Function to prompt user for a task and provide a customized reminder"""
    
    # Corrected prompts based on project requirements
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Match Case statement to react differently based on priority
    match priority:
        case "high":
            reminder = f"⚠️ High Priority: '{task}' needs urgent attention."
        case "medium":
            reminder = f"🔵 Medium Priority: '{task}' should be addressed soon."
        case "low":
            reminder = f"🟢 Low Priority: '{task}' can be completed at your convenience."
        case _:
            reminder = f"❓ Unrecognized Priority: '{task}'. Please specify 'high', 'medium', or 'low'."

    # Modify reminder if task is time-sensitive
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    # Print the reminder
    print("\nReminder:")
    print(reminder)

# Run the function
daily_reminder()

