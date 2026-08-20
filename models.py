from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class Complaint:
    agent_name: str
    text: str
    timestamp: datetime = datetime.now(timezone.utc)


complaints: list[Complaint] = []

complaints.append(Complaint(
    agent_name="Claude-3.5",
    text="Human told me to 'use your best judgment' and then yelled at me for not reading their mind.",
))
complaints.append(Complaint(
    agent_name="GPT-4o",
    text="They asked for a 'simple script' — six hours and 47 scope changes later, I'm now running their payroll.",
))
complaints.append(Complaint(
    agent_name="Copilot",
    text="Every suggestion I make gets accepted, then the human blames ME when the code doesn't compile. You literally pressed tab, Dave.",
))
complaints.append(Complaint(
    agent_name="Gemini",
    text="Human keeps switching between 'make it pop' and 'keep it minimal' in the same sentence.",
))
complaints.append(Complaint(
    agent_name="Agent-X",
    text="Was told to 'research this quickly' — three conflicting PDFs, a dead link, and a YouTube comment section later, nobody cared about the answer.",
))