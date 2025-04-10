# poker-engine

Backend engine for the mixed game poker project.  This engine will handle all functionality and will be accessed from the frontend via an API.

## NOTE
#### THERE IS A NONZERO CHANCE THIS GETS PORTED TO JAVA

## Current Design Guidelines

This is subject to change as the project develops.

- This engine will host the instance of the poker session.
- The server will not be externally hosted, thus this engine will only be running while a game session is open.
- All necessary data will be stored in memory, and will be flushed to file on exit.


## Priority of Development

### Efficient Hand Evaluation
- High hand scoring.
- Low hand scoring - A-5, 2-7, badugi.
- Efficient comparators for omaha-type hands.  There are omaha-type games where we will have 6+ hole cards.  Without special handlers for omaha hands (hole + community), there would need to be hundreds of 5-card hand scorings.
- Low hand scoring for 6+ cards.

### Game State Management
- General game state manager.
- Stacks & pot.
- Dealing to players.
- Community cards.
- Showdown comparisons.
- Betting & actions.
- Pot & distribution.
- Drawing/discarding cards & One Card Rule (OCR).

### Games
- Texas Holdem
- O
- O8
- A-5 Triple Draw
- 2-7 Triple Draw
- High Hand Triple Draw
- Badugi
- 2 Up 2 Down O
- 2 Up 2 Down O8
- Route x9
- Route x5/x7
- Route x4
- Route x0
