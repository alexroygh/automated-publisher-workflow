def human_feedback_loop(content):
    print("🧠 AI Output:\n", content)
    print("\n✍️ Enter your feedback/edit below. Press ENTER twice to finish.\n")

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "" and lines:
                break
            lines.append(line)
        except KeyboardInterrupt:
            break

    user_input = "\n".join(lines).strip()
    return user_input if user_input else content
