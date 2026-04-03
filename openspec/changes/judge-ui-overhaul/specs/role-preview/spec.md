## ADDED Requirements

### Requirement: Role pool is fixed per player count
The system SHALL maintain a fixed role pool for each supported player count (6 and 8). The pool composition is determined solely by the player count and cannot be modified at runtime.

#### Scenario: 6-player role pool
- **WHEN** the judge selects 6-player mode
- **THEN** the role pool contains: 1 Werewolf, 1 Hidden Werewolf, 1 Prophet, 1 Witch, 1 Hunter, 1 Guard, 1 Duplicate, 5 Villagers (12 cards total)

#### Scenario: 8-player role pool
- **WHEN** the judge selects 8-player mode
- **THEN** the role pool contains: 2 Werewolves, 1 Hidden Werewolf, 1 Prophet, 1 Witch, 1 Hunter, 1 Guard, 1 Idiot, 1 Silencer, 1 Duplicate, 6 Villagers (16 cards total)

### Requirement: Shuffle produces valid assignment
The system SHALL shuffle the role pool into pairs (2 cards per player) such that:
- No player receives Prophet paired with Werewolf or Hidden Werewolf
- At least one player receives a "safe" pair: (Villager, Villager), (Duplicate, Villager), or (Villager, Duplicate)

#### Scenario: Invalid pair is rejected
- **WHEN** a shuffle produces Prophet paired with Werewolf for any player
- **THEN** the assignment is rejected and a new shuffle is attempted

#### Scenario: No safe pair is rejected
- **WHEN** a shuffle produces no player with a safe pair
- **THEN** the assignment is rejected and a new shuffle is attempted

### Requirement: Judge can preview full assignment
The system SHALL display the complete shuffled assignment (all players and their two roles) to the judge before distribution begins.

#### Scenario: Preview shows all players
- **WHEN** a valid shuffle is generated
- **THEN** the judge sees a table listing every player number with their two assigned roles

### Requirement: Judge can accept or re-shuffle
The system SHALL allow the judge to either accept the current assignment or request a new shuffle.

#### Scenario: Judge accepts assignment
- **WHEN** the judge chooses to accept the current assignment
- **THEN** the system proceeds to the distribution phase

#### Scenario: Judge requests re-shuffle
- **WHEN** the judge chooses to re-shuffle
- **THEN** the system generates a new valid assignment and displays it for preview
