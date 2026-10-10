## Purpose

The author-style profile lets each author create and manage a private writing preference from their own writing. It prevents a shared writing assistant from treating one author's voice as the default for everyone.

## ADDED Requirements

### Requirement: Style onboarding SHALL be optional

The assistant SHALL offer writing-style analysis as an optional setup path. Skipping this path SHALL NOT block the author from starting an article.

#### Scenario: Author skips style setup

- **WHEN** the author chooses not to provide samples or analyze an account
- **THEN** the assistant proceeds to ask what the author wants to write without claiming to know their personal style

### Requirement: Account-level style analysis SHALL require explicit scope and consent

Before analyzing an account, the assistant SHALL ask whether the author wants selected samples analyzed or account-level analysis. For account-level analysis, it SHALL obtain explicit consent and let the author select the source and time range. It SHALL analyze only accessible original writing attributable to that author.

#### Scenario: Author chooses selected samples

- **WHEN** the author provides selected writing samples
- **THEN** the assistant analyzes only those samples for the requested style profile

#### Scenario: Author chooses account-level analysis

- **WHEN** the author selects an account and time range and explicitly consents to analysis
- **THEN** the assistant analyzes accessible original posts in that scope and reports any source or coverage limitations

#### Scenario: Account source is inaccessible

- **WHEN** a selected account or post cannot be accessed
- **THEN** the assistant explains the limitation and asks the author to paste the content or provide an export without requesting account credentials

### Requirement: A style profile SHALL be reviewed before persistence

The assistant SHALL produce a concise style summary and a short sample rewrite for author review. It SHALL save a profile only after explicit author approval.

#### Scenario: Author corrects the style summary

- **WHEN** the author disagrees with a style observation or sample rewrite
- **THEN** the assistant revises the proposed profile and requests review again

#### Scenario: Author approves persistence

- **WHEN** the author explicitly approves saving the profile
- **THEN** the assistant stores it as that author's profile and confirms that it can be viewed, edited, or deleted

#### Scenario: Author does not approve persistence

- **WHEN** the author reviews the summary but declines to save it
- **THEN** the assistant uses it only for the current session and does not persist it

### Requirement: Author profiles SHALL be isolated and user-controlled

Each author's profile SHALL be private to that author, SHALL NOT be included in shared Agent or Skill defaults, and SHALL support viewing, editing, and deletion. Article-specific facts, opinions, and drafts SHALL NOT be added to a long-term profile automatically.

#### Scenario: Different authors use the same shared Agent

- **WHEN** two authors use the same shared Agent with different profiles
- **THEN** each receives only their own approved preferences and neither author's profile changes the other's behavior

#### Scenario: Author asks to inspect or remove a profile

- **WHEN** an author asks to view, edit, or delete their saved profile
- **THEN** the assistant shows the current profile, applies the requested edit, or removes it and confirms the result

### Requirement: A style profile SHALL support a shared voice and optional platform variants

The profile SHALL support one shared voice plus optional platform-specific preferences without requiring separate profiles for every platform.

#### Scenario: Author uses a platform-specific variant

- **WHEN** the author requests writing for a platform with a saved variant
- **THEN** the assistant applies the shared voice and that platform's approved variant

#### Scenario: Author has no platform variant

- **WHEN** the author requests writing for a platform without a saved variant
- **THEN** the assistant applies the shared voice and follows the requested platform format without inventing a saved preference
