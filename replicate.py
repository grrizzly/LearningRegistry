#!/usr/bin/env python
import couchdb, sys
from util import *

def replacate_across_servers(main_url, replication_servers, database_name):
    couch = couchdb.Server(main_url)
    for replication in replication_servers:
        create_database(replication['url'],replication['db_name'])
        couch.replicate(database_name,replication['url']+ replication['db_name'])
if __name__ == '__main__':
    main_url = 'http://localhost/'
    server_database = 'knowservers'
    database_name = 'learningregistry'
    replication_servers =  []
    db = get_database(main_url,server_database)
    for i in db:        
        replication_servers.append(db[i])    
    replacate_across_servers(main_url,replication_servers, database_name)