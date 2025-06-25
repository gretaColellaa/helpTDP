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


#Somma stipendi per team in un certo anno
SELECT t.year, t.name, SUM(s.salary)
FROM teams t JOIN salaries s ON t.ID = s.teamID
WHERE t.year = 1985
GROUP BY t.year, t.ID, t.name;

#Giocatori con media goal > x
SELECT a.playerID
FROM actions a
GROUP BY a.playerID
HAVING AVG(a.goals) > 0.5;

#Elenco delle gare per anno

SELECT r.raceId, r.name, c.name AS circuito, r.date
FROM races r
JOIN circuits c ON r.circuitId = c.circuitId
WHERE r.year = 2012
ORDER BY r.date;

# Vittorie di ogni pilota in un anno

SELECT d.driverId, d.forename, d.surname, COUNT(*) AS vittorie
FROM results res
JOIN drivers d ON res.driverId = d.driverId
JOIN races r ON res.raceId = r.raceId
WHERE res.position = 1 AND r.year = 2012
GROUP BY d.driverId
ORDER BY vittorie DESC;


#pilota che ha battuto più avversari
SELECT winner.driverId, d.forename, d.surname, COUNT(*) AS vittorie_totali
FROM results winner
JOIN results loser ON winner.raceId = loser.raceId
    AND winner.position < loser.position
JOIN drivers d ON winner.driverId = d.driverId
WHERE winner.position IS NOT NULL AND loser.position IS NOT NULL
GROUP BY winner.driverId
ORDER BY vittorie_totali DESC
LIMIT 1;


#coppie di gare per cui almeno k piloti hanno ottenuto una posizione not null
WITH gare AS (
  SELECT r.raceId, r.circuitId, r.date, c.name AS circuito
  FROM races r
  JOIN circuits c ON r.circuitId = c.circuitId
  WHERE r.year = %s
),
piloti_validi AS (
  SELECT r.raceId, r.driverId
  FROM results r
  WHERE r.position IS NOT NULL
),
coppie_gare AS (
  SELECT
    g1.raceId AS raceId1,
    g2.raceId AS raceId2,
    g1.circuito AS circuito1,
    g2.circuito AS circuito2
  FROM gare g1
  JOIN gare g2 ON g1.date < g2.date AND g1.circuitId <> g2.circuitId
)
SELECT
  cg.raceId1, cg.raceId2, cg.circuito1, cg.circuito2,
  COUNT(*) AS piloti_in_comune
FROM coppie_gare cg
JOIN piloti_validi p1 ON p1.raceId = cg.raceId1
JOIN piloti_validi p2 ON p2.raceId = cg.raceId2 AND p1.driverId = p2.driverId
GROUP BY cg.raceId1, cg.raceId2, cg.circuito1, cg.circuito2
HAVING COUNT(*) >= %s
ORDER BY piloti_in_comune DESC;

#4. Costruzione del grafo delle vittorie
#Per ciascuna coppia (A, B), contare quante volte A è arrivato prima di B:

SELECT r1.driverId AS vincente, r2.driverId AS sconfitto, COUNT(*) AS vittorie
FROM results r1
JOIN results r2 ON r1.raceId = r2.raceId
WHERE r1.position IS NOT NULL AND r2.position IS NOT NULL
  AND r1.position < r2.position
  AND r1.driverId != r2.driverId
GROUP BY vincente, sconfitto;
#✅ Output: archi orientati con peso = numero di vittorie dirette. Può essere usato per costruire il grafo.

#🏗️ 1. Elenco dei costruttori (constructors)

SELECT constructorId, name, nationality
FROM constructors
ORDER BY name;
#✅ Elenco di tutte le scuderie con la loro nazionalità.

#🏁 2. Gare disputate su un certo circuito

SELECT r.name AS nome_gara, r.date, c.name AS circuito
FROM races r
JOIN circuits c ON r.circuitId = c.circuitId
WHERE c.name = 'Monza'
ORDER BY r.date DESC;
✅ Gare corse a Monza, ordinate dalla più recente.

#‍🔧 3. Piloti di una determinata scuderia

SELECT DISTINCT d.driverId, d.forename, d.surname
FROM results res
JOIN drivers d ON res.driverId = d.driverId
JOIN constructors c ON res.constructorId = c.constructorId
WHERE c.name = 'Ferrari'
ORDER BY d.surname;
#✅ Piloti che almeno una volta hanno corso per la Ferrari.

#⏱️ 4. Tempo medio di gara di un pilota
#Questa richiede che la tabella lap_times o simili sia disponibile, ma se volessimo calcolare media della posizione come proxy:


SELECT d.driverId, d.forename, d.surname, AVG(res.position) AS media_posizione
FROM results res
JOIN drivers d ON res.driverId = d.driverId
WHERE res.position IS NOT NULL
GROUP BY d.driverId
ORDER BY media_posizione ASC
LIMIT 10;
#✅ Piloti con media di posizione migliore (più vicini alla 1ª posizione).

#🏆 5. Pilota con più pole position in un anno

SELECT d.driverId, d.forename, d.surname, COUNT(*) AS pole_position
FROM qualifying q
JOIN drivers d ON q.driverId = d.driverId
JOIN races r ON q.raceId = r.raceId
WHERE q.position = 1 AND r.year = 2022
GROUP BY d.driverId
ORDER BY pole_position DESC;
#✅ Pilota con più pole nel 2022 (richiede la tabella qualifying).

#🏎️ 6. Vittorie per costruttore in un anno

SELECT c.name AS costruttore, COUNT(*) AS vittorie
FROM results res
JOIN constructors c ON res.constructorId = c.constructorId
JOIN races r ON res.raceId = r.raceId
WHERE res.position = 1 AND r.year = 2022
GROUP BY c.name
ORDER BY vittorie DESC;
#✅ Scuderie con più vittorie nel 2022.

#🔁 7. Gare con podio completo (top 3)

SELECT r.name AS gara, r.date, d.forename, d.surname, res.position
FROM results res
JOIN races r ON res.raceId = r.raceId
JOIN drivers d ON res.driverId = d.driverId
WHERE res.position <= 3
ORDER BY r.date, res.position;
#✅ Podio di tutte le gare, ordinato per data e posizione.