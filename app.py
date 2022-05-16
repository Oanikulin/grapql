from api import app, db
from api import models
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.queries import listOngoingGames_resolver, listFinishedGames_resolver, getGameScoreboard_resolver
query = ObjectType("Query")
query.set_field("listOngoingGames", listOngoingGames_resolver)
query.set_field("listFinishedGames", listFinishedGames_resolver)
query.set_field("getGameScoreboard", getGameScoreboard_resolver)

from api.mutations import *
mutation = ObjectType("Mutation")
mutation.set_field("createOngoingGame", createOngoingGame_resolver)
mutation.set_field("finishGame", finishGame_resolver)
mutation.set_field("addComment", addComment_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    print('graphql request', flush=True)
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code