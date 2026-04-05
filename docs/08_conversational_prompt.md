# 08. Conversational Prompt

![Conversational prompt explained with a banking example](../visuals/conversational_prompt.png)

## What it is

A conversational prompt uses a back-and-forth interaction instead of a single instruction.

The model can ask clarifying questions before giving a stronger answer.

## Banking fundamentals example

```text
User: I need a bank account.
AI: What matters most: low fees, high interest, or mobile access?
```

This turns a vague request into a guided conversation.

## When to use it

Use conversational prompting when:

- the user goal is underspecified
- follow-up questions improve the answer
- the task is interactive by nature

Example use cases:

- account selection assistant
- loan intake assistant
- branch support chatbot

## Why it works

The model can gather missing context instead of guessing too early.

## Limitations

It depends on good follow-up questions and solid memory across the conversation.

## Banking tip

This prompt type is especially effective in customer-service or product-assistant scenarios.
