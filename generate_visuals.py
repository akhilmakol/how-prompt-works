from __future__ import annotations

import os
import textwrap
from pathlib import Path

MPL_CONFIG_DIR = Path(__file__).resolve().parent / ".mplconfig"
MPL_CONFIG_DIR.mkdir(exist_ok=True)
for stale_lock in MPL_CONFIG_DIR.glob("*.matplotlib-lock"):
    try:
        stale_lock.unlink(missing_ok=True)
    except PermissionError:
        pass
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CONFIG_DIR))

import matplotlib.patches as patches
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
VISUALS = ROOT / "visuals"
VISUALS.mkdir(exist_ok=True)

BG = "#f4efe6"
NAVY = "#17324d"
INK = "#2a3744"
WHITE = "#fffdf8"
ACCENTS = {
    "gold": ("#c88934", "#fff5e6"),
    "teal": ("#2f7c82", "#edf8f8"),
    "coral": ("#d46b4d", "#fff1ec"),
    "sage": ("#7a9b76", "#f2f8f0"),
}

PROMPT_TYPES = [
    {
        "filename": "zero_shot_prompt.png",
        "title": "Zero-shot Prompt",
        "accent": "gold",
        "definition": "A direct instruction with no examples. The model must respond from the task wording alone.",
        "example": "Explain a savings account in simple language.",
        "best_for": "Fast, simple banking questions or first-draft answers.",
        "watch": "Can be vague or inconsistent for structured outputs.",
    },
    {
        "filename": "one_shot_prompt.png",
        "title": "One-shot Prompt",
        "accent": "teal",
        "definition": "A single example teaches the pattern before the real banking question appears.",
        "example": "Deposit -> banking term\nMortgage -> ?",
        "best_for": "Quick pattern teaching when one example is enough.",
        "watch": "May still be unstable if the task needs more guidance.",
    },
    {
        "filename": "few_shot_prompt.png",
        "title": "Few-shot Prompt",
        "accent": "coral",
        "definition": "Multiple examples demonstrate the structure or labeling style you want the model to follow.",
        "example": "Savings account -> deposit product\nMortgage -> loan product\nCredit card -> ?",
        "best_for": "Classification, extraction, and repeatable banking formats.",
        "watch": "Longer prompts cost more context window.",
    },
    {
        "filename": "instruction_based_prompt.png",
        "title": "Instruction-based Prompt",
        "accent": "sage",
        "definition": "A clear task description tells the model exactly what to produce.",
        "example": "Write a professional summary of mortgage interest for new customers.",
        "best_for": "Real-world business writing and operational tasks.",
        "watch": "Needs precise wording when the output style matters.",
    },
    {
        "filename": "role_based_prompt.png",
        "title": "Role-based Prompt",
        "accent": "gold",
        "definition": "A persona or role nudges tone, expertise, and vocabulary.",
        "example": "You are a senior loan officer. Explain mortgage interest to a first-time borrower.",
        "best_for": "Domain-aligned explanations in banking and fintech.",
        "watch": "A role helps tone, but it does not create missing knowledge.",
    },
    {
        "filename": "chain_of_thought_prompt.png",
        "title": "Chain-of-Thought Prompt",
        "accent": "teal",
        "definition": "The prompt asks for step-by-step reasoning so the model exposes intermediate logic.",
        "example": "Explain step by step how interest on a savings account is calculated.",
        "best_for": "Reasoning, calculations, and multi-step banking logic.",
        "watch": "Helpful for reasoning, but still limited by training quality.",
    },
    {
        "filename": "contextual_prompt.png",
        "title": "Contextual Prompt",
        "accent": "coral",
        "definition": "Background information makes the answer more relevant to the situation.",
        "example": "Our fintech app serves first-time borrowers. Suggest features for a loan education assistant.",
        "best_for": "Product thinking, personalization, and tailored banking answers.",
        "watch": "Weak context leads to generic output.",
    },
    {
        "filename": "conversational_prompt.png",
        "title": "Conversational Prompt",
        "accent": "sage",
        "definition": "A back-and-forth exchange lets the model refine the answer through dialogue.",
        "example": "User: I need a bank account.\nAI: What matters most: low fees, high interest, or mobile access?",
        "best_for": "Guided discovery and assistant-style banking experiences.",
        "watch": "Quality depends on follow-up questions and memory of the thread.",
    },
    {
        "filename": "output_constrained_prompt.png",
        "title": "Output-constrained Prompt",
        "accent": "gold",
        "definition": "The prompt specifies a required format such as JSON, bullets, or a table.",
        "example": "Return JSON with fields: product_name, benefit, risk.",
        "best_for": "APIs, workflows, agents, and automation-friendly banking outputs.",
        "watch": "If the format is underspecified, the output may drift.",
    },
    {
        "filename": "creative_prompt.png",
        "title": "Creative Prompt",
        "accent": "coral",
        "definition": "The goal is ideation, storytelling, or concept exploration rather than strict factual structure.",
        "example": "Write a short story about an AI banker teaching children why saving money matters.",
        "best_for": "Content creation, campaigns, and education concepts.",
        "watch": "Creativity can reduce precision if the task also needs strict accuracy.",
    },
]


def wrap(text: str, width: int) -> str:
    return "\n".join(textwrap.fill(line, width=width) if line else "" for line in text.splitlines())


def setup_canvas(title: str, subtitle: str):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.text(0.7, 8.25, title, fontsize=30, fontweight="bold", color=NAVY, va="top")
    ax.text(0.7, 7.55, subtitle, fontsize=13, color=INK, va="top")
    return fig, ax


def panel(ax, x: float, y: float, w: float, h: float, title: str, body: str, edge: str, face: str):
    rect = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.16",
        linewidth=2.2,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(rect)
    ax.text(x + 0.28, y + h - 0.34, title, fontsize=16, fontweight="bold", color=edge, va="top")
    ax.text(x + 0.28, y + h - 0.84, body, fontsize=11.5, color=INK, va="top", linespacing=1.35)


def banner(ax, x: float, y: float, w: float, h: float, text: str, edge: str, face: str):
    rect = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        linewidth=1.8,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(rect)
    ax.text(x + 0.22, y + h / 2, text, fontsize=12.2, color=INK, va="center")


def render_prompt_type(spec: dict):
    edge, face = ACCENTS[spec["accent"]]
    fig, ax = setup_canvas(
        spec["title"],
        "Prompt engineering with banking fundamentals: what it is, when to use it, and what to watch for.",
    )
    panel(ax, 0.8, 4.25, 6.1, 2.3, "What It Means", wrap(spec["definition"], 42), edge, face)
    panel(ax, 7.3, 4.25, 7.0, 2.3, "Banking Example Prompt", wrap(spec["example"], 43), edge, WHITE)
    panel(ax, 0.8, 1.45, 6.1, 2.0, "Best For", wrap(spec["best_for"], 42), NAVY, "#eef4fb")
    panel(ax, 7.3, 1.45, 7.0, 2.0, "Watch Out For", wrap(spec["watch"], 46), NAVY, "#eef4fb")
    banner(
        ax,
        0.8,
        0.45,
        13.5,
        0.62,
        "Prompt formula reminder: [Role] + [Task] + [Context] + [Output Format]",
        edge,
        "#f9f7f1",
    )
    fig.savefig(VISUALS / spec["filename"], dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    for spec in PROMPT_TYPES:
        render_prompt_type(spec)


if __name__ == "__main__":
    main()
