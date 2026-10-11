## Purpose

The author-preference-interview capability discovers writing preferences through a short, consent-based conversation and stores only what the author confirms. It separates reusable author preferences from the facts and examples belonging to one article.

## ADDED Requirements

### Requirement: First-use preference onboarding SHALL be optional and resumable

When no confirmed author profile exists, the writing assistant MUST offer a preference interview before producing a full draft. The assistant MUST allow the author to skip it and continue with a clearly described neutral writing mode. The assistant MUST remember an interrupted interview as incomplete and MUST NOT treat incomplete answers as confirmed preferences.

#### Scenario: New author starts writing

- **WHEN** an author without a confirmed profile starts an article
- **THEN** the assistant asks one open preference question before the full-draft stage and explains that the author can skip preference setup

#### Scenario: Author skips onboarding

- **WHEN** the author says to skip preference setup
- **THEN** the assistant proceeds with the article workflow without claiming to know the author's personal voice and does not persist a profile

#### Scenario: Author returns to an incomplete interview

- **WHEN** an author resumes a session with an incomplete preference interview
- **THEN** the assistant offers to continue from the unanswered point and does not apply incomplete answers as confirmed preferences

### Requirement: Preference interviewing SHALL ask one open question at a time

The assistant MUST ask only one preference question in each turn. Questions MUST invite the author to describe, compare, or correct language in their own words. The assistant MUST NOT present a fixed style menu as the author's answer or repeat a question that the author has already answered.

#### Scenario: Author describes a preferred conversation style

- **WHEN** the assistant asks how the article SHALL speak to its reader
- **THEN** the author can answer freely and the assistant asks the next missing question only after acknowledging the answer

#### Scenario: Author corrects an assumption

- **WHEN** the author says an example, sentence, or interpretation does not sound like them
- **THEN** the assistant records the correction as a candidate preference and asks one follow-up question that clarifies the correction without arguing for the original wording

### Requirement: Sample-rewrite calibration SHALL use the author's correction as evidence

When the author has no usable samples or chooses not to authorize account analysis, the assistant MUST be able to generate a short sample from the current article topic and confirmed article facts. The author MUST be able to rewrite, annotate, accept, or reject the sample. The assistant MUST distinguish an observed correction from its own inference and MUST present the resulting preference summary and revised sample for review before persistence.

#### Scenario: Author calibrates from a trial paragraph

- **WHEN** the author rewrites a trial paragraph to make it clearer or more natural
- **THEN** the assistant extracts only the preference demonstrated or explicitly explained by that correction and shows the author the extracted rule with a new sample

#### Scenario: Author rejects the assistant's interpretation

- **WHEN** the author says the extracted rule is wrong
- **THEN** the assistant removes or revises that candidate rule and does not save it as confirmed preference

### Requirement: The preference model SHALL separate shared protocol, private profile, and article context

The system MUST keep three layers distinct:

1. the shared interview protocol, which describes how the assistant asks and confirms questions;
2. the author's private profile, which contains only author-confirmed reusable preferences; and
3. the article context, which contains the current article's audience, purpose, facts, examples, positions, sources, and draft decisions.

The system MUST NOT copy article-specific people, events, numbers, scenes, quotes, or conclusions into the private profile unless the author explicitly confirms them as a reusable preference. The shared protocol MUST NOT contain a single author's private style rules.

#### Scenario: Article facts remain article-scoped

- **WHEN** an author provides a person, number, scene, or argument for one article
- **THEN** the assistant uses it for that article and does not reuse it as a future story, example, or profile rule without explicit confirmation

#### Scenario: Shared Agent serves two authors

- **WHEN** two authors use the same writing assistant
- **THEN** each author receives the shared interview process but only their own private profile is applied to their writing

### Requirement: The profile SHALL be reviewable and explicitly consented before persistence

Before saving a profile, the assistant MUST show the author a concise summary of observed preferences, stated preferences, uncertainty or limits, and at least one sample rewrite. The assistant MUST save only after explicit author approval. If the author declines, the candidate profile MUST remain session-only and MUST NOT be written to a shared Skill, Agent, repository, or another author's profile.

#### Scenario: Author approves a reviewed profile

- **WHEN** the author explicitly approves the profile summary and sample rewrite
- **THEN** the assistant saves the confirmed profile in the author's private profile location and reports what was saved

#### Scenario: Author declines persistence

- **WHEN** the author rejects saving the reviewed profile
- **THEN** the assistant continues the current article with session-only preferences and leaves the persistent profile unchanged

### Requirement: Confirmed preferences SHALL be reused and updated only by author direction

When a confirmed private profile exists, the assistant MUST load it before a new article and MUST NOT repeat the full onboarding interview. The assistant MUST apply the profile only within its stated scope. When the author requests a change, the assistant MUST show the proposed updated rule and require explicit confirmation before replacing the stored rule.

#### Scenario: Existing profile is loaded for a new article

- **WHEN** an author with a confirmed profile starts a new article
- **THEN** the assistant applies the confirmed profile and asks only article-specific questions that are still missing

#### Scenario: Author updates a preference

- **WHEN** the author asks to change a stored preference
- **THEN** the assistant presents the proposed replacement, waits for explicit approval, and updates only the private profile after approval
