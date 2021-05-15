# philia
A slack bot for keeping you from hurting a co-worker's feelings

## Problem

Healthy communication between co-workers provides great value for companies. However, when people get caught up on tasks and busyness, it's hard to ensure the receiver's awareness of an emotionally loaded message and, therefore, their ability to respond accordingly. For example,

(A **worker 1** sends a message about being late to a project due date):

*I'm so sorry, I know I should end by now.*

(A **worker 2** receives this message, and being in the middle of a meeting-busy-, answer):

*Complete it immediately.*

As we can imagine, this answer could make **worker 1** stress worse.

It can be a better way, what if **worker 2**, has an assessment of its answer in terms of emotional load at the moment of sending it so it can double check how appropriate is its answer to the text (like a differential between the receive and answered message). Specifically a slack bot can be created to provide this assessment.

## Development

### Lint

- black
- isort
- flake8

### Local testing

**Local Deployment**

```bash
# With all the slack-api/requirements.txt in place
cd slack-api/
chalice local
```

### Deployment

```bash
# With all the slack-api/requirements.txt in place
cd slack-api/
chalice deploy
```
