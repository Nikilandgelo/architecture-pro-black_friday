from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import errors

from .settings import client, DATABASE_NAME


async def get_shards_info(collection_names: list[str]) -> dict:
    try:
        shards_list = await client.admin.command("listShards")
    except errors.OperationFailure:
        return {}

    shard_clients = {}
    for shard in shards_list.get("shards", []):
        host = shard["host"]  # e.g. "shard1/mongo_shard_1:27018"
        if "/" in host:
            replset_name, hosts = host.split("/", 1)
            uri = f"mongodb://{hosts}/?replicaSet={replset_name}"
        else:
            uri = f"mongodb://{host}/"

        shard_clients[shard["_id"]] = AsyncIOMotorClient(uri)

    info = {}
    for shard_id, shard_client in shard_clients.items():
        try:
            status = await shard_client.admin.command("replSetGetStatus")
            members = status.get("members", [])
            replica_info = {
                "instances_count": len(members),
                "primary": next(
                    (m["name"] for m in members if m["stateStr"] == "PRIMARY"), None
                ),
                "secondaries": [
                    m["name"] for m in members if m["stateStr"] == "SECONDARY"
                ],
            }
        except errors.OperationFailure:
            replica_info = {"replica_count": 1, "primary": None, "secondaries": []}

        shard_db = shard_client[DATABASE_NAME]
        collections = {}
        for collection_name in collection_names:
            collection = shard_db.get_collection(collection_name)
            collections[collection_name] = {
                "documents_count": await collection.count_documents({})
            }

        info[shard_id] = {**replica_info, "collections": collections}

    return info
