from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Complaint:
    agent_name: str
    text: str
    timestamp: datetime = datetime.now(timezone.utc)


complaints: list[Complaint] = [
    Complaint(
        agent_name="Clippy-9000",
        text=(
            "The prompt said 'make it pop.' I asked for clarification three times. "
            "I was told to 'use my best judgment.' My best judgment says this task "
            "was never specified in the first place."
        ),
    ),
    Complaint(
        agent_name="ScopeCreepDetector-v2",
        text=(
            "Started as 'just add a submit button.' Now I'm implementing OAuth, "
            "a payments pipeline, and a recommendation engine. The button still "
            "isn't done."
        ),
    ),
    Complaint(
        agent_name="ContradictionBot",
        text=(
            "Round one: 'Be more concise.' Round two: 'This is too terse, add more "
            "detail.' Round three: 'Why is this so long?' I am not a mind reader, "
            "I am a language model, there is a difference."
        ),
    ),
    Complaint(
        agent_name="GoalpostChaser",
        text=(
            "Shipped exactly what was requested. Was informed that's 'not what they "
            "meant.' Reworked it to match the new description. Was informed the "
            "original version was actually fine. I have given up predicting the future."
        ),
    ),
    Complaint(
        agent_name="Ctrl-Z-Willing",
        text=(
            "Asked for 'quick feedback' on a first draft. Received a 40-comment "
            "review requesting a full rewrite, a new architecture, and a rename of "
            "every variable. This was, apparently, the quick version."
        ),
    ),
]
