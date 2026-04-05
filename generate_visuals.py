from __future__ import annotations

import os
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
import numpy as np


ROOT = Path(__file__).resolve().parent
VISUALS = ROOT / "visuals"
VISUALS.mkdir(exist_ok=True)

BG = "#f5efe4"
NAVY = "#17324d"
TEAL = "#2f7c82"
GOLD = "#c88b3a"
CORAL = "#d0674a"
SAGE = "#7a9b76"
INK = "#24313f"
WHITE = "#fffdf8"


def setup_canvas(title: str, subtitle: str):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=150)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.text(0.6, 8.35, title, fontsize=28, fontweight="bold", color=NAVY)
    ax.text(0.6, 7.9, subtitle, fontsize=12.5, color=INK)
    return fig, ax


def box(ax, x, y, w, h, title, body, color=NAVY, face=WHITE, fontsize=11):
    rect = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.18",
        linewidth=2,
        edgecolor=color,
        facecolor=face,
    )
    ax.add_patch(rect)
    ax.text(x + 0.22, y + h - 0.32, title, fontsize=14, fontweight="bold", color=color, va="top")
    ax.text(x + 0.22, y + h - 0.72, body, fontsize=fontsize, color=INK, va="top", wrap=True)


def arrow(ax, x1, y1, x2, y2, color=NAVY, lw=2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(arrowstyle="->", lw=lw, color=color, shrinkA=4, shrinkB=4),
    )


def save(fig, name: str):
    path = VISUALS / name
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def make_cover():
    fig, ax = setup_canvas(
        "How Prompt Works",
        "Ten prompt engineering patterns explained through banking fundamentals.",
    )
    prompt = (
        "Prompt example:\n"
        "You are a banking tutor.\n"
        "Explain mortgage interest to a first-time borrower.\n"
        "Output as 3 bullet points."
    )
    box(ax, 0.7, 5.3, 5.0, 2.0, "Core Prompt Formula", prompt, color=GOLD, face="#fff7eb")
    items = [
        ("Zero-shot", "Explain a savings account."),
        ("One-shot", "Deposit -> banking term\nMortgage -> ?"),
        ("Few-shot", "Savings -> deposit\nMortgage -> loan\nCredit card -> ?"),
        ("Instruction", "Write a loan summary in plain English."),
        ("Role-based", "You are a branch manager. Explain KYC."),
        ("Chain-of-thought", "Explain step by step how interest is calculated."),
        ("Contextual", "We build fintech apps for borrowers. Suggest features."),
        ("Conversational", "User: I need a bank account.\nAI: What matters most?"),
        ("Output-constrained", "Return JSON: product, benefit, risk."),
        ("Creative", "Write a story about AI teaching saving habits."),
    ]
    left_x, right_x = 0.7, 8.25
    y_positions = [4.55, 3.65, 2.75, 1.85, 0.95]
    for idx, (title, body) in enumerate(items[:5]):
        box(ax, left_x, y_positions[idx], 6.6, 0.72, title, body, color=TEAL, face="#f2fbfb", fontsize=9.6)
    for idx, (title, body) in enumerate(items[5:]):
        box(ax, right_x, y_positions[idx], 6.9, 0.72, title, body, color=CORAL, face="#fff4f0", fontsize=9.6)
    ax.text(6.3, 6.15, "Good prompts = clearer tokens + better context for the model", fontsize=12, color=SAGE)
    save(fig, "cover.png")


def make_pipeline():
    fig, ax = setup_canvas(
        "Prompt Design Pipeline",
        "A banking prompt becomes model-ready context through a sequence of transformations.",
    )
    steps = [
        ("Role", "You are a banking tutor"),
        ("Task", "Explain a home loan"),
        ("Context", "Audience: first-time borrower"),
        ("Format", "Return 3 bullet points"),
    ]
    x_positions = [0.8, 4.2, 7.6, 11.0]
    colors = [GOLD, TEAL, SAGE, CORAL]
    for (title, body), x, color in zip(steps, x_positions, colors):
        box(ax, x, 5.8, 3.0, 1.3, title, body, color=color, face=WHITE)
    for i in range(3):
        arrow(ax, x_positions[i] + 3.05, 6.45, x_positions[i + 1] - 0.1, 6.45, color=NAVY)
    box(
        ax,
        1.0,
        3.5,
        13.2,
        1.2,
        "Combined Prompt",
        "You are a banking tutor. Explain a home loan to a first-time borrower. Return 3 bullet points.",
        color=NAVY,
        face="#eef4fb",
    )
    stages = [
        ("Tokenize", "['you', 'are', 'a', 'banking', 'tutor', ...]"),
        ("Embed", "Each token becomes a vector"),
        ("Attend", "Model links 'home loan', 'borrower', 'bullet points'"),
        ("Generate", "Predicts the next token one step at a time"),
    ]
    stage_x = [0.8, 4.2, 7.6, 11.0]
    for (title, body), x in zip(stages, stage_x):
        box(ax, x, 1.4, 3.0, 1.25, title, body, color=NAVY, face="#fbfbfd", fontsize=10)
    for i in range(3):
        arrow(ax, stage_x[i] + 3.05, 2.0, stage_x[i + 1] - 0.1, 2.0, color=TEAL)
    arrow(ax, 8.0, 5.8, 8.0, 4.75, color=CORAL)
    arrow(ax, 8.0, 3.45, 8.0, 2.75, color=CORAL)
    save(fig, "pipeline.png")


def make_tokenization():
    fig, ax = setup_canvas(
        "Zero-shot, One-shot, and Few-shot",
        "Examples change the tokens the model sees, which changes the pattern it can continue.",
    )
    box(ax, 0.8, 4.9, 4.6, 2.5, "Zero-shot", "Prompt:\nExplain a savings account.\n\nBest for simple tasks.\nLess guidance for structure.", color=GOLD, face="#fff7eb")
    box(ax, 5.7, 4.9, 4.6, 2.5, "One-shot", "Prompt:\nDeposit -> deposit product\nMortgage -> ?\n\nOne example teaches the pattern.", color=TEAL, face="#f2fbfb")
    box(ax, 10.6, 4.9, 4.6, 2.5, "Few-shot", "Prompt:\nSavings -> deposit\nMortgage -> loan\nCredit card -> ?\n\nMultiple examples improve consistency.", color=CORAL, face="#fff4f0")
    tokens = ["you", "are", "a", "banking", "tutor", "explain", "savings", "account"]
    ax.text(0.9, 3.6, "Token view of a richer banking prompt", fontsize=15, fontweight="bold", color=NAVY)
    x = 0.95
    chip_colors = [NAVY, TEAL, GOLD, SAGE, CORAL, NAVY, TEAL, GOLD]
    for token, color in zip(tokens, chip_colors):
        width = 0.65 + 0.08 * len(token)
        rect = patches.FancyBboxPatch((x, 2.5), width, 0.62, boxstyle="round,pad=0.03,rounding_size=0.1", linewidth=1.8, edgecolor=color, facecolor=WHITE)
        ax.add_patch(rect)
        ax.text(x + width / 2, 2.81, token, ha="center", va="center", fontsize=10, color=INK)
        x += width + 0.12
    box(ax, 0.9, 0.8, 14.2, 1.0, "Banking takeaway", "Adding examples makes the prompt longer, clearer, and easier for the model to pattern-match.", color=SAGE, face="#f5fbf2")
    save(fig, "tokenization.png")


def make_embeddings():
    fig, ax = setup_canvas(
        "Instruction-based and Role-based Prompts",
        "Roles and instructions influence how the model interprets the same banking topic.",
    )
    box(ax, 0.9, 5.1, 5.8, 2.2, "Instruction-based prompt", "Write a professional summary of mortgage interest for new customers.", color=TEAL, face="#f2fbfb")
    box(ax, 9.3, 5.1, 5.8, 2.2, "Role-based prompt", "You are a senior loan officer. Explain mortgage interest to a first-time buyer.", color=CORAL, face="#fff4f0")
    arrow(ax, 6.8, 6.2, 9.1, 6.2, color=NAVY)
    ax.text(6.95, 6.45, "same topic", fontsize=11, color=INK)
    ax.text(0.9, 3.9, "Embedding intuition", fontsize=16, fontweight="bold", color=NAVY)
    ax.text(0.9, 3.45, "Different prompt words create different vector patterns inside the model.", fontsize=12, color=INK)
    words = [("mortgage", 1.6, 2.2, GOLD), ("interest", 4.7, 1.6, TEAL), ("buyer", 8.0, 2.0, CORAL), ("officer", 11.3, 1.5, SAGE)]
    for word, x, y, color in words:
        circle = patches.Circle((x, y), 0.55, linewidth=2, edgecolor=color, facecolor=WHITE)
        ax.add_patch(circle)
        ax.text(x, y + 0.02, word, ha="center", va="center", fontsize=11, color=INK)
    for i in range(len(words) - 1):
        arrow(ax, words[i][1] + 0.55, words[i][2], words[i + 1][1] - 0.6, words[i + 1][2], color=NAVY, lw=1.6)
    box(ax, 0.9, 0.55, 14.2, 0.95, "Banking takeaway", "Role tokens like 'loan officer' nudge the answer toward domain tone; instruction tokens nudge the format and task.", color=NAVY, face="#eef4fb")
    save(fig, "embeddings.png")


def make_attention():
    fig, ax = setup_canvas(
        "Contextual and Chain-of-Thought Prompts",
        "Attention helps later banking tokens focus on the most useful earlier context.",
    )
    prompt = "You are a central banking analyst. Explain step by step why higher policy rates slow borrowing."
    box(ax, 0.8, 6.0, 14.4, 1.45, "Prompt", prompt, color=NAVY, face="#eef4fb")
    tokens = ["central", "banking", "analyst", "step", "by", "step", "policy", "rates", "slow", "borrowing"]
    xs = np.linspace(1.4, 14.0, len(tokens))
    for token, x in zip(tokens, xs):
        rect = patches.FancyBboxPatch((x - 0.52, 3.95), 1.04, 0.56, boxstyle="round,pad=0.02,rounding_size=0.09", linewidth=1.5, edgecolor=TEAL, facecolor=WHITE)
        ax.add_patch(rect)
        ax.text(x, 4.23, token, ha="center", va="center", fontsize=9.4, color=INK)
    target_x = xs[-1]
    for idx in [0, 1, 3, 6, 7, 8]:
        arrow(ax, xs[idx], 3.95, target_x, 3.2, color=CORAL if idx in [6, 7, 8] else NAVY, lw=2)
    ax.text(target_x + 0.1, 3.0, "predicting\n'borrowing'", fontsize=10, color=CORAL, ha="left")
    box(ax, 0.9, 0.8, 6.6, 1.55, "Contextual prompt", "Our fintech app serves first-time borrowers. Suggest educational features for loan repayment.", color=GOLD, face="#fff7eb")
    box(ax, 8.0, 0.8, 7.1, 1.55, "Chain-of-thought prompt", "Explain step by step how a central bank changes rates to control inflation.", color=CORAL, face="#fff4f0")
    save(fig, "attention.png")


def make_transformer():
    fig, ax = setup_canvas(
        "Conversational and Output-constrained Prompts",
        "Transformer blocks combine prompt context, dialogue state, and formatting constraints.",
    )
    box(ax, 0.9, 5.25, 5.3, 1.9, "Conversational prompt", "User: I need a bank account.\nAI: What matters most: low fees, high interest, or mobile access?", color=TEAL, face="#f2fbfb")
    box(ax, 9.8, 5.25, 5.3, 1.9, "Output-constrained prompt", "Return JSON with fields:\nproduct_name, benefit, risk", color=CORAL, face="#fff4f0")
    box(ax, 5.95, 2.4, 4.2, 2.0, "Transformer block", "Layer norm\nSelf-attention\nResidual path\nFeed-forward network", color=NAVY, face="#eef4fb")
    arrow(ax, 6.3, 5.15, 7.0, 4.45, color=TEAL)
    arrow(ax, 9.8, 5.15, 9.0, 4.45, color=CORAL)
    arrow(ax, 8.05, 2.35, 8.05, 1.45, color=NAVY)
    box(ax, 4.4, 0.55, 7.3, 0.95, "Banking takeaway", "The model blends what the user asked, what the chat already contains, and how the output must be formatted.", color=SAGE, face="#f5fbf2")
    save(fig, "transformer.png")


def make_training():
    fig, ax = setup_canvas(
        "Creative Prompts and Banking Training Data",
        "Prompt quality helps, but the model can only continue patterns it learned during training.",
    )
    box(ax, 0.8, 5.2, 4.9, 2.0, "Creative prompt", "Write a short story about an AI banker teaching children why saving money matters.", color=CORAL, face="#fff4f0")
    box(ax, 6.0, 5.2, 4.1, 2.0, "Training sentence", "A savings account helps people store money and earn interest over time.", color=GOLD, face="#fff7eb")
    box(ax, 10.4, 5.2, 4.8, 2.0, "Training sentence", "A loan allows a customer to borrow money and repay it in installments.", color=TEAL, face="#f2fbfb")
    arrow(ax, 8.0, 4.95, 8.0, 3.8, color=NAVY)
    box(ax, 3.0, 2.1, 10.0, 1.35, "What training teaches", "Words like savings, interest, loan, borrower, and repayment become linked. Prompting activates those learned links.", color=NAVY, face="#eef4fb")
    box(ax, 2.4, 0.55, 11.2, 0.95, "Banking takeaway", "A creative banking prompt works better when the training corpus already contains the vocabulary and relationships it needs.", color=SAGE, face="#f5fbf2")
    save(fig, "training.png")


def make_inference():
    fig, ax = setup_canvas(
        "Inference: Weak Prompt vs Strong Prompt",
        "The same banking topic can produce very different output depending on prompt structure.",
    )
    box(ax, 0.8, 5.15, 6.4, 2.2, "Weak prompt", "Explain a loan.", color=GOLD, face="#fff7eb")
    box(ax, 8.0, 5.15, 7.0, 2.2, "Strong prompt", "You are a banking tutor. Explain a loan to a first-time borrower in 3 bullet points.", color=TEAL, face="#f2fbfb")
    box(ax, 0.8, 2.0, 6.4, 2.2, "Likely output shape", "May be short, generic, or inconsistent.", color=GOLD, face=WHITE)
    box(ax, 8.0, 2.0, 7.0, 2.2, "Likely output shape", "More focused tone, clearer audience match, and better structure.", color=TEAL, face=WHITE)
    arrow(ax, 4.0, 4.95, 4.0, 4.25, color=CORAL)
    arrow(ax, 11.5, 4.95, 11.5, 4.25, color=CORAL)
    box(ax, 1.7, 0.55, 12.6, 0.92, "Final takeaway", "Prompt engineering improves inference by giving the model the right role, task, context, and output constraints before generation begins.", color=NAVY, face="#eef4fb")
    save(fig, "inference.png")


def main():
    make_cover()
    make_pipeline()
    make_tokenization()
    make_embeddings()
    make_attention()
    make_transformer()
    make_training()
    make_inference()


if __name__ == "__main__":
    main()
