EXPLAIN SELECT NameDepartement 
    FROM Departement JOIN Commune ON Commune.IdDepartement = Departement.IdDepartement 
    WHERE NameCommune = 'Paris';

-- Output 
-- "Nested Loop  (cost=0.00..693.32 rows=1 width=10)"
-- "  Join Filter: ((departement.iddepartement)::text = (commune.iddepartement)::text)"
-- "  ->  Seq Scan on commune  (cost=0.00..688.05 rows=1 width=3)"
-- "        Filter: ((namecommune)::text = 'Paris'::text)"
-- "  ->  Seq Scan on departement  (cost=0.00..4.01 rows=101 width=13)"


EXPLAIN SELECT CodeCommune
    FROM DeptChefLieu JOIN Departement ON DeptChefLieu.IdDepartement = Departement.IdDepartement 
    WHERE NameDepartement = 'Orne';

-- Output 
-- "Hash Join  (cost=4.28..6.56 rows=1 width=6)"
-- "  Hash Cond: ((deptcheflieu.iddepartement)::text = (departement.iddepartement)::text)"
-- "  ->  Seq Scan on deptcheflieu  (cost=0.00..2.01 rows=101 width=9)"
-- "  ->  Hash  (cost=4.26..4.26 rows=1 width=3)"
-- "        ->  Seq Scan on departement  (cost=0.00..4.26 rows=1 width=3)"
-- "              Filter: ((namedepartement)::text = 'Orne'::text)"