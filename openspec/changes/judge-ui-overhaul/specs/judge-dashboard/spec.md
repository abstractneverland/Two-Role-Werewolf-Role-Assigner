## ADDED Requirements

### Requirement: Dashboard displays all player roles
The system SHALL display a persistent table showing every player's top and bottom roles after distribution is complete.

#### Scenario: Full table rendered
- **WHEN** distribution is complete
- **THEN** the dashboard shows a table with columns: Player, Top Role, Bottom Role

### Requirement: Dead roles displayed with strikethrough
The system SHALL render dead roles with a strikethrough visual effect (Unicode combining characters) while alive roles display normally.

#### Scenario: Alive role displays normally
- **WHEN** a role is alive
- **THEN** the role name is displayed as plain text

#### Scenario: Dead role displays with strikethrough
- **WHEN** a role is dead
- **THEN** the role name is displayed with strikethrough (e.g., V̶i̶l̶l̶a̶g̶e̶r̶)

### Requirement: Judge can mark role as dead
The system SHALL allow the judge to mark a specific role (top or bottom) of a specific player as dead via a command.

#### Scenario: Mark top role dead
- **WHEN** the judge enters the command to kill player 3's top role
- **THEN** that role is marked dead and the dashboard re-renders with strikethrough

#### Scenario: Mark bottom role dead
- **WHEN** the judge enters the command to kill player 3's bottom role
- **THEN** that role is marked dead and the dashboard re-renders with strikethrough

### Requirement: Judge can restore role as alive
The system SHALL allow the judge to restore a dead role to alive status via a command.

#### Scenario: Restore dead role
- **WHEN** the judge enters the command to revive player 3's top role
- **THEN** that role is marked alive and the dashboard re-renders without strikethrough

### Requirement: Dashboard refreshes on state change
The system SHALL re-render the dashboard table after any role state change (kill or revive).

#### Scenario: Dashboard updates after kill
- **WHEN** a role is marked dead
- **THEN** the dashboard immediately re-renders showing the updated state

### Requirement: Dashboard remains interactive
The system SHALL keep the dashboard interactive, accepting commands until the judge chooses to quit.

#### Scenario: Judge enters quit command
- **WHEN** the judge enters the quit command
- **THEN** the system exits cleanly

#### Scenario: Invalid command handled
- **WHEN** the judge enters an unrecognized command
- **THEN** the system displays a help message and re-renders the dashboard
