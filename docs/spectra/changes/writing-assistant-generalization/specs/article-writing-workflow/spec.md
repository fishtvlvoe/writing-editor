## Purpose

The article-writing workflow guides an author from an initial idea through interview, research, outline, drafting, revision, and author-approved delivery. It keeps the author in control of the topic, position, and final text.

## ADDED Requirements

### Requirement: The writing assistant SHALL interview one question at a time

The writing assistant SHALL ask one open-ended question per turn and SHALL use the author's answers to choose the next question. It SHALL NOT present a preset answer as the author's choice or assume the author's position.

#### Scenario: Continue an interview from the author's answer

- **WHEN** the author answers an interview question
- **THEN** the assistant asks one relevant follow-up question and does not bundle multiple interview questions into the same turn

#### Scenario: Author is unsure

- **WHEN** the author says they do not know or are not ready to answer
- **THEN** the assistant helps them think with an open prompt or a smaller question without supplying a preferred answer

### Requirement: The writing assistant SHALL separate suggestions from the author's position

The assistant SHALL provide brainstorming ideas only when the author explicitly asks for ideation. It SHALL label those ideas as suggestions and SHALL NOT use them as the author's position in an outline or draft until the author confirms them.

#### Scenario: Author requests ideas

- **WHEN** the author explicitly asks the assistant to brainstorm
- **THEN** the assistant offers clearly labeled ideas and asks which, if any, the author wants to use

#### Scenario: No ideation request

- **WHEN** the author is being interviewed without asking for brainstorming
- **THEN** the assistant asks open-ended questions and does not insert unrequested positions or examples

### Requirement: The writing assistant SHALL confirm the article direction and outline before drafting

The assistant SHALL identify the intended reader, article purpose, author-confirmed position, source boundaries, and proposed outline before drafting. It SHALL wait for author confirmation of the direction and outline.

#### Scenario: Unclear article direction

- **WHEN** the author has not confirmed the intended reader, purpose, or position
- **THEN** the assistant continues interviewing and does not advance to drafting

#### Scenario: Outline approval

- **WHEN** the assistant presents an outline for the article
- **THEN** it waits for the author's approval or requested changes before producing the full draft

### Requirement: The writing assistant SHALL verify external factual claims when research is needed

The assistant SHALL distinguish author-provided experience and opinion from external claims that require evidence. It SHALL identify sources for researched claims and clearly mark claims it cannot verify.

#### Scenario: Claim can be verified

- **WHEN** a draft depends on an external factual claim
- **THEN** the assistant checks an appropriate source and records the supporting source in the working materials

#### Scenario: Claim cannot be verified

- **WHEN** the assistant cannot verify an external claim or finds conflicting evidence
- **THEN** it marks the uncertainty and does not present the claim as confirmed fact

### Requirement: The writing assistant SHALL draft and revise within the confirmed direction

The assistant SHALL produce a complete article draft from confirmed interview material, the approved outline, and verified facts. It SHALL revise in response to author feedback while preserving the confirmed position unless the author changes it.

#### Scenario: Author requests a revision

- **WHEN** the author requests a change to wording, emphasis, or structure
- **THEN** the assistant revises the relevant text and keeps the rest aligned with the approved position

#### Scenario: Author changes the central position

- **WHEN** the author's feedback changes the central position or intended reader
- **THEN** the assistant returns to the relevant interview or outline confirmation step before continuing the draft

### Requirement: The writing assistant SHALL require author approval before marking an article final

The assistant SHALL check factual support, argument continuity, intended reader, author voice, privacy boundaries, and requested format before asking for final approval. It SHALL mark an article as final only after explicit author approval.

#### Scenario: Author has not approved the final draft

- **WHEN** the assistant has completed its quality checks but the author has not approved the draft
- **THEN** the article remains a draft

#### Scenario: Author approves the final draft

- **WHEN** the author explicitly approves the article
- **THEN** the assistant marks that version as final and delivers it in the requested format

### Requirement: The writing assistant SHALL not publish without explicit instruction

The assistant SHALL treat final article delivery and external publication as separate actions.

#### Scenario: Final article is approved without a publish request

- **WHEN** the author approves the article but does not request publication
- **THEN** the assistant delivers the article and does not publish, post, or send it externally

### Requirement: The first release SHALL focus on social posts and web articles

The writing assistant SHALL support social posts, blog posts, and web articles in the first release. It SHALL NOT claim support for unrelated document types as part of this capability.

#### Scenario: Author requests an in-scope article

- **WHEN** the author requests a social post, blog post, or web article
- **THEN** the assistant follows the interview-to-final workflow

#### Scenario: Author requests an out-of-scope document type

- **WHEN** the author requests an email, proposal, or report
- **THEN** the assistant states that the first-release workflow is focused on articles and asks whether the author wants to adapt the request into an article
