## ADDED Requirements

### Requirement: Cards displayed visually during distribution
The system SHALL display each player's two roles as visual "cards" in the terminal, showing both role names and their current top/bottom positions.

#### Scenario: Cards rendered for player
- **WHEN** it is a player's turn to receive their roles
- **THEN** the terminal displays two card boxes side by side, each containing one role name and a position label (TOP CARD / BOTTOM CARD)

### Requirement: Player can swap card positions
The system SHALL allow the player to swap the top and bottom card positions by pressing the Space key. The display SHALL update immediately to reflect the swap.

#### Scenario: Space key swaps cards
- **WHEN** the player presses Space during card selection
- **THEN** the two cards exchange positions and the display is re-rendered

#### Scenario: Multiple swaps allowed
- **WHEN** the player presses Space multiple times
- **THEN** the cards toggle positions with each press

### Requirement: Player confirms selection with Enter
The system SHALL finalize the card arrangement when the player presses Enter, recording which role is top and which is bottom.

#### Scenario: Enter confirms and proceeds
- **WHEN** the player presses Enter during card selection
- **THEN** the system records the top/bottom arrangement and proceeds to the next player

### Requirement: Screen cleared between players
The system SHALL clear the terminal screen between each player's distribution to prevent role leakage to other players.

#### Scenario: Screen cleared before next player
- **WHEN** one player's distribution is complete
- **THEN** the screen is cleared before the next player is prompted
