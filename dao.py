def getNodes(anno, metodo):
    conn = DBConnect.get_connection()

    result = []

    cursor = conn.cursor(dictionary=True)
    query = """ ****
    """

    cursor.execute(query, (anno, metodo))

    for row in cursor:
        result.append(row)

    cursor.close()
    conn.close()
    return result
