from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select your transport with a defined url endpoint
transport = AIOHTTPTransport(url="http://0.0.0.0:5000/graphql")

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

while (True):
  command = input()
  params = None
  if (command == 'list ongoing'):
    # Provide a GraphQL query
    query = gql(
    """
    query listOngoingGames {
      listOngoingGames {
        success
        errors
        games {
          id
          finished
          comments
        }
      }
    }
    """
    )
  elif (command == 'list finished'):
    # Provide a GraphQL query
    query = gql(
    """
    query listFinishedGames {
      listFinishedGames {
        success
        errors
        games {
          id
          finished
          comments
        }
      }
    }
    """
    )

  elif (command == 'get game'):
    ind = input()
    params = {"ind" : ind}
    query = gql(
    """
    query getGameScoreboard($ind: ID!) {
      getGameScoreboard (id: $ind) {
        success
        errors
        scoreboard {
          id
          names
          victory
        }
      }
    }
    """
    )

  elif (command == 'start game'):
    query = gql(
    """
    mutation createOngoingGame {
      createOngoingGame {
        success
        errors
      }
    }
    """
    )

  elif (command == 'finish game'):
    ind = input()
    names = list(input().split())
    results = list(input().split())
    if (len(names) != len(results)):
      print('Length in scoreboard do not match')
      continue
    params = {"ind" : ind, "names" : names, "results" : results}
    query = gql(
    """
    mutation finishGame($ind: ID!, $names: [String], $results: [String]) {
      finishGame (id: $ind, names: $names, result: $results) {
        success
        errors
        scoreboard {
          id
          names
          victory
        }
      }
    }
    """
    )
  elif (command == 'add comment'):
    ind = input()
    comment = input()
    params = {"ind" : ind, "comment" : comment}
    query = gql(
    """
    mutation finishGame($ind: ID!, $comment: [String]) {
      addComment (id: $ind, comment: $comment) {
        success
        error
      }
    }
    """
    )
  else:
    print('Command not undestood')
    continue

  # Execute the query on the transport
  result = client.execute(query, variable_values=params)
  print(result)