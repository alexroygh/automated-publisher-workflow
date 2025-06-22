from ai_agents.ai_writer import ai_writer
from ai_agents.ai_reviewer import ai_reviewer
from ai_agents.ai_editor import ai_editor
import re
import tiktoken

def split_text(text, max_tokens=2000):
    
    enc = tiktoken.encoding_for_model("gpt-4")
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks = []
    current_chunk = ""
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = len(enc.encode(sentence))
        if current_tokens + sentence_tokens <= max_tokens:
            current_chunk += sentence + " "
            current_tokens += sentence_tokens
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "
            current_tokens = sentence_tokens

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def get_multiline_input(prompt_msg="📝 Enter your input (type 'END' on a new line to finish):"):
    print(prompt_msg)
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def agentic_flow(chapter):
    print("📖 Original Chapter:")
    print(chapter)

    chunks = split_text(chapter, max_tokens=2000)
    outputs = []

    for i, chunk in enumerate(chunks):
        print(f"\n--- Processing Chunk {i+1}/{len(chunks)} ---")

        # Writing phase
        draft = ai_writer(chunk)
        print("\n✍️ AI Writer Output:\n", draft)
        use_draft = input("🔁 Use this draft as-is? (y/n): ")
        if use_draft.lower() != 'y':
            revised_draft = get_multiline_input(
                "\n📝 Enter your revised draft (or press ENTER to keep AI version). Type 'END' to finish:"
            )
            if revised_draft:
                draft = revised_draft

        # Review phase
        review = ai_reviewer(draft)
        print("\n🧐 AI Reviewer Output:\n", review)
        use_review = input("🔁 Use this reviewed version as-is? (y/n): ")
        if use_review.lower() != 'y':
            revised_review = get_multiline_input(
                "\n📝 Enter your revised review (or press ENTER to keep AI version). Type 'END' to finish:"
            )
            if revised_review:
                review = revised_review

        # Edit phase
        edited = ai_editor(review)
        print("\n🖋️ AI Editor Output:\n", edited)

        final_text = edited
        while True:
            edit_choice = input("\n🔁 Would you like to revise this edited chunk again before finalization? (y/n): ")
            if edit_choice.lower() == 'y':
                user_edit = get_multiline_input(
                    "\n📝 Enter your updated version (or press ENTER to keep current version). Type 'END' to finish:"
                )
                if user_edit:
                    final_text = user_edit
                print("\n✅ Updated Text:\n", final_text)
            elif edit_choice.lower() == 'n':
                break
            else:
                print("Please enter 'y' or 'n'.")

        outputs.append(final_text.strip())

    final_output = "\n\n".join(outputs)
    return final_output

