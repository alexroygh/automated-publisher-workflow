def human_feedback_loop(content):
    print("AI Output:\n", content)
    print("\nEnter your feedback or edit. Press ENTER to keep as-is.")
    user_input = input("> ")
    return user_input if user_input.strip() else content
