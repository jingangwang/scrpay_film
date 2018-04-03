db_config = {
    'test': {
        'host': "10.6.2.50", 'port': 3309,
        'user': "mayong", 'passwd': "MaYong",
        'db': "test", 'charset': "utf8",
        'pool': {
            # use = 0 no pool else use pool
            "use": 1,
            # size is >=0,  0 is dynamic pool
            "size": 10,
            # pool name
            "name": "test-pool",
        }
    },

}
