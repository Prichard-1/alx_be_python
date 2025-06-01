def daily_reminder():
    """Function to prompt user for a task and provide a customized reminder"""
    
    # Prompt user for task details
    task = input("Enter the task description: ")
    priority = input("Enter the task priority (high, medium, low): ").lower()
    time_bound = input("Is the task time-bound? (yes or no): ").lower()

    # Match Case statement to react differently based on priority
    match priority:
        case "high":
            reminder = f"⚠️ High Priority: {task} needs urgent attention."
        case "medium":
            reminder = f"🔵 Medium Priority: {task} should be addressed soon."
        case "low":
            reminder = f"🟢 Low Priority: {task} can be completed at your convenience."
        case _:
            reminder = f"❓ Unrecognized Priority: {task}. Please specify 'high', 'medium', or 'low'."

    # Modify reminder if task is time-sensitive
    if time_bound == "yes":
        reminder += " That requires immediate attention today!"

    # Print the reminder
    print("\nReminder:")
    print(reminder)

# Run the function
daily_reminder()

