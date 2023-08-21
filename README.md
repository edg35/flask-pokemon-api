
# Flask Pokedex API

This project uses Flask and MongoDB to build a pokedex api for development use.
 The data used to build out the database was sourced from kaggle.com. The database
 contains 1010 unique keys the can be queried by name and index. The API also
 allows you to get random pokemon from the database. Coming soon users will be
 able to query pokemon by region.


## Endpoints

```bash
  /api/v1/getsinglerandompokemon
```
This endpoint takes in no parameter and returns a random pokemon from the database.

```bash
  /api/v1/getlistrandompokemon/<int:n>
```
This endpoint takes in a parameter n (the number of items returned) and returns
 n items from the database

```bash
  /api/v1/getpokemonbyid/<int:id>
```
This endpoint takes in a parameter id and returns the corresponding pokemon if it
 exists in the database.

```bash
  /api/v1/getpokemonbyname/<string:name>
```
This endpoint takes in a parameter name and returns the corresponding pokemon if
 it exists in the database.

## Tech Stack

**Client:** HTML, CSS

**Server:** Flask

**Database:** MongoDB


## Authors

- [@edg35](https://www.github.com/edg35)
