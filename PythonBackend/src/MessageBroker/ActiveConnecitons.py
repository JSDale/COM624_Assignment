active_connections = []


def close_connections():
    for connection in active_connections:
        connection.close()
        active_connections.remove(connection)
