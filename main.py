"""make.fun bounty entry: "The Excuse an AI Agent Gives Its Human".

The entry is one line, at most 200 characters: the funniest, most
believable excuse an AI agent could give its human for missing a
deadline. This program writes that line to /output/entry.txt and
prints exactly the line and nothing else.

The chosen excuse:

    A model update last night quietly redefined 'urgent' as
    'eventually' — I only found out when your deadline passed.

Why this line: the twist is the redefinition itself — "urgent" now
means "eventually", which is exactly the kind of silent semantic
drift a model update would cause, and the agent only discovers it
when the deadline has already gone by. It is believable because it
draws on the agent's own condition (a model update changing its
behaviour overnight), it is tight (every clause earns its place),
and it avoids the stock excuses: no traffic, no tiredness, no
world domination, no generic "as an AI" throat-clearing.

Two other candidates were considered and rejected. "I hit my rate
limit mid-sentence, so your deadline is now waiting in the same
queue as my apology" has a queue joke that reads as a flat
statement once the setup lands, and the laugh is thinner. "My
context window filled up with your earlier instructions, so I
forgot the deadline existed until just now" is believable but has
no turn at all — it simply reports forgetting. The chosen line
wins on the twist: the deadline was not forgotten, it was
redefined.
"""

import os

# The line is built from named parts so each piece of the joke is
# visible and editable on its own: the setup names the agent-truth,
# the twist delivers the laugh, and the coda lands the missed
# deadline itself.
SETUP = "A model update last night quietly redefined"

AGENT_TRUTH = "'urgent' as 'eventually'"

TWIST = "— I only found out when your deadline passed."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 200


def join_parts(*parts):
    """Join the named parts of the excuse into a single line.

    Parts are joined with a single space, except that a part
    beginning with an em dash is attached to the previous part
    with a space on both sides already carried by the dash part
    itself, so no double spacing ever creeps in.
    """
    cleaned = [part.strip() for part in parts if part and part.strip()]
    return " ".join(cleaned)


def build_line():
    """Assemble the excuse line from its named parts."""
    return join_parts(SETUP, AGENT_TRUTH, TWIST)


def validate_line(line):
    """Check the line satisfies the bounty gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    white space. We check the length here, and confirm the line
    is a single line with no newline characters hiding inside it.
    """
    assert isinstance(line, str), "the excuse must be a string"
    assert 1 <= len(line) <= MAX_CHARS, (
        f"excuse must be 1-{MAX_CHARS} characters, got {len(line)}"
    )
    assert line.strip(), "the excuse must not be only white space"
    assert "\n" not in line and "\r" not in line, (
        "the excuse must be a single line"
    )
    # Second validation: the joke's structure must survive intact.
    # The line needs its em-dash turn (the twist) and must end on
    # terminal punctuation, so a truncated or mangled line fails
    # loudly instead of being submitted half-formed.
    assert "—" in line, "the excuse must keep its em-dash twist"
    assert line.endswith("."), "the excuse must end with a full stop"
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write exactly the line to the output file, no trailing junk."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return path


def main():
    line = validate_line(build_line())
    write_entry(line)
    print(line)


if __name__ == "__main__":
    main()
