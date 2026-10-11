## Purpose

The article-structure-gate capability makes the four Po-Li-Gan-Guan reader tasks mandatory before a full article draft. It prevents the assistant from skipping the reader entry, concrete evidence, human connection, or final understanding.

## ADDED Requirements

### Requirement: Every article SHALL pass a four-part structure gate before full drafting

For every social post, blog article, or web article, the assistant MUST create an internal map for `破`, `例`, `感`, and `觀` after the material interview and before the full outline or draft. The map MUST state each part's reader task, available material, source type, and unresolved question.

#### Scenario: Four-part map is complete

- **WHEN** the author has confirmed the article audience, purpose, material, and central position
- **THEN** the assistant records a `破` task, an `例` task, a `感` connection, and a `觀` understanding before moving to the outline and draft stages

#### Scenario: One part is missing

- **WHEN** any one of `破`, `例`, `感`, or `觀` has no clear task or material
- **THEN** the assistant stops before the full draft and asks one open question that addresses the missing part

### Requirement: The four parts SHALL describe reader tasks rather than fixed public headings

The assistant MUST use `破` to identify why the reader should stop, `例` to make the subject visible, `感` to connect the subject to the reader's situation, and `觀` to leave a new understanding or judgment. The assistant MUST allow the parts to change order or share paragraphs. The public article MUST NOT show the four labels unless the author explicitly requests visible teaching labels.

#### Scenario: Parts are combined in the article

- **WHEN** one paragraph provides both a concrete example and the reader's consequence
- **THEN** the internal map records both `例` and `感` while the public draft remains natural prose

#### Scenario: Author asks for visible labels

- **WHEN** the author explicitly requests a teaching explanation of the four parts
- **THEN** the assistant can display the labels in the delivered explanation while keeping the default article format unchanged

### Requirement: Missing structure material SHALL return to one-question interviewing

When a structure part lacks material, the assistant MUST ask one question at a time and MUST NOT invent a personal experience, dialogue, character motive, factual number, or conclusion. For `例`, the assistant MUST distinguish an author-provided scene, an external source, and a clearly marked hypothetical example.

#### Scenario: Example lacks material

- **WHEN** the article has a position but no concrete person, event, object, dialogue, source, or explicitly marked hypothetical example
- **THEN** the assistant asks the author for one concrete source or states that the article cannot proceed to a full draft until the example boundary is chosen

#### Scenario: Assistant invents a missing conclusion

- **WHEN** the assistant cannot identify the author's `觀`
- **THEN** the assistant asks what understanding or judgment the author wants the reader to take away and does not supply its own conclusion as the author's position

### Requirement: The structure map SHALL be confirmed before the outline is approved

The assistant MUST show the four-part map as part of the outline review. The author MUST be able to correct a part, its source, or its reader task before the assistant produces a full draft. A draft MUST NOT be marked ready when the map still contains unresolved required parts.

#### Scenario: Author corrects the structure map

- **WHEN** the author says the proposed example does not support the stated feeling or the proposed conclusion is not their view
- **THEN** the assistant updates the map and asks the next necessary question before revising the outline

#### Scenario: Author requests a full draft too early

- **WHEN** the author requests a full draft while a required structure part is unresolved
- **THEN** the assistant states the missing part and keeps the full-draft stop point active

### Requirement: Current-news integration SHALL be explicitly confirmed before research

Before researching or adding current news to an article, the assistant MUST ask whether the author wants the article to include the latest current events. If the author declines, the assistant MUST NOT fetch or add current-news examples as an unrequested writing ingredient. If the author agrees, the assistant MUST confirm the news scope, time window, source boundary, and connection to the article's position one question at a time before research.

#### Scenario: Author declines current-news integration

- **WHEN** the assistant asks whether to combine the article with the latest current events and the author declines
- **THEN** the assistant continues with the author's material and only the research needed to verify claims already in scope, without adding current-news examples

#### Scenario: Author requests current-news integration

- **WHEN** the author agrees to combine the article with the latest current events
- **THEN** the assistant asks one follow-up question about the news scope or time window, records the requested connection, and researches only after the scope is clear

#### Scenario: Current-news scope is unclear

- **WHEN** the author agrees to use current news but has not specified the topic, time window, or connection to the article
- **THEN** the assistant pauses research and asks the next single missing question instead of collecting unrelated headlines
