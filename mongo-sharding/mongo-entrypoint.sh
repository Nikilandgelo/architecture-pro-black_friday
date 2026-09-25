#!/bin/sh

mongosh --host mongo_config_1 --port 27020 --eval '
  try {
    rs.initiate({_id: "configSrv", configsvr: true, members: [
      {_id: 0, host: "mongo_config_1:27020"},
      {_id: 1, host: "mongo_config_2:27021"},
      {_id: 2, host: "mongo_config_3:27022"}
    ]});
  } catch(e) { print(e); }
'

mongosh --host mongo_shard_1 --port 27018 --eval '
  try {
    rs.initiate({_id: "shard1", members: [{_id: 0, host: "mongo_shard_1:27018"}]});
  } catch(e) { print(e); }
'

mongosh --host mongo_shard_2 --port 27019 --eval '
  try {
    rs.initiate({_id: "shard2", members: [{_id: 0, host: "mongo_shard_2:27019"}]});
  } catch(e) { print(e); }
'

until mongosh --host mongo_config_1 --port 27020 --eval 'rs.status().myState' | grep -q 1; do
  echo waiting for configSrv primary...
  sleep 1
done
