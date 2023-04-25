
-- Bloquer toutes les modifications sur la table REGION
CREATE RULE block_region_insert AS ON INSERT TO Region DO INSTEAD NOTHING;
CREATE RULE block_region_update AS ON UPDATE TO Region DO INSTEAD NOTHING;
CREATE RULE block_region_delete AS ON DELETE TO Region DO INSTEAD NOTHING;

-- Bloquer toutes les modifications sur la table DEPARTEMENT
CREATE RULE block_departement_insert AS ON INSERT TO Departement DO INSTEAD NOTHING;
CREATE RULE block_departement_update AS ON UPDATE TO Departement DO INSTEAD NOTHING;
CREATE RULE block_departement_delete AS ON DELETE TO Departement DO INSTEAD NOTHING;

-- Create a trigger function that calls the CalculatePopulation procedure
CREATE OR REPLACE FUNCTION update_population() RETURNS trigger AS $$
BEGIN
    ALTER TABLE Region DISABLE RULE block_region_update;
    ALTER TABLE Departement DISABLE RULE block_departement_update;
    CALL CalculateRegionPopulation(NEW.StartYear);
    ALTER TABLE Region ENABLE RULE block_region_update;
    ALTER TABLE Departement ENABLE RULE block_departement_update;
    RETURNS NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger on the Statistic table
CREATE TRIGGER update_population_trigger
AFTER INSERT OR UPDATE OR DELETE ON Statistic
FOR EACH ROW
EXECUTE PROCEDURE update_population();

---- To test update_population(), we change Paris' population in 2019.
-- (2019) 75056 --> 2165423
SELECT * FROM Statistic 
WHERE codeCommune = '75056' AND startyear = 2019 AND category = 'Population en 2019';

SELECT * FROM Region;

-- Set Paris' population in 2019 to 0.
UPDATE Statistic 
SET statvalue = 0
WHERE codeCommune = '75056' AND startyear = 2019 AND category = 'Population en 2019';

-- We observe the modification of the PopulationRegion column in Region for 2019 (NEW.StartYear).
SELECT * FROM Region;

-- To undo the change:
UPDATE Statistic 
SET statvalue = 2165423
WHERE codeCommune = '75056' AND startyear = 2019 AND category = 'Population en 2019';
