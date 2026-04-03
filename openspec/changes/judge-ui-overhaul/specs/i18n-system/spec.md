## ADDED Requirements

### Requirement: Language selection at startup
The system SHALL prompt the judge to select a language (English or 中文) before any game logic begins. The selection SHALL apply to all UI text and role names for the entire session.

#### Scenario: English selected
- **WHEN** the judge selects English at startup
- **THEN** all prompts, messages, and role names are displayed in English

#### Scenario: Chinese selected
- **WHEN** the judge selects 中文 at startup
- **THEN** all prompts, messages, and role names are displayed in Chinese

#### Scenario: Invalid language selection
- **WHEN** the judge enters an invalid language option
- **THEN** the system re-prompts for a valid selection

### Requirement: All UI text resolved through translation layer
The system SHALL resolve all user-facing strings through a centralized translation layer keyed by language and string identifier.

#### Scenario: Role name translation
- **WHEN** the system needs to display a role name
- **THEN** it looks up the role name in the translation table for the current language

#### Scenario: UI prompt translation
- **WHEN** the system needs to display a UI prompt
- **THEN** it looks up the prompt text in the translation table for the current language

### Requirement: Role names consistent across languages
The system SHALL maintain a one-to-one mapping between English and Chinese role names. Every role in the English pool SHALL have a corresponding Chinese translation.

#### Scenario: Werewolf translation
- **WHEN** the role "Werewolf" is displayed in Chinese mode
- **THEN** it is rendered as "狼人"

#### Scenario: All 6-player roles translatable
- **WHEN** the system runs in Chinese mode with 6 players
- **THEN** all role names (狼人, 隐狼, 预言家, 女巫, 猎人, 守卫, 盗贼, 平民) are correctly displayed
