def human_feedback_loop(content):
    print("🧠 AI Output:\n", content)
    print("\n✍️ Enter your feedback/edit below. (type 'END' on a new line to finish)\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    user_input = "\n".join(lines).strip()
    return user_input if user_input else content
