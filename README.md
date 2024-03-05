# RESTingway

Yet another FFXIV Game data API
Planned to not only include FFXIV game data, but also other services like Universalis and Lodestone

Yes, there are enough other tools that can do the exact same thing than this is planned to do.

## Testing

http://127.0.0.1:8000/docs

## Tech
- python
- FastAPI

## Modules
- parsingway: parses game data from csv files
- routingway: all REST routes, and related operations
- storingway: stores game data in a database, and handels all database queries
- connectingway: connects to external services like Universalis and Lodestone

## Resources
- gamedata/ffxiv-datamining/ is the result of ```git clone https://github.com/xivapi/ffxiv-datamining```
- universalis docs: https://universalis.app/docs