
-- For Stored procedure EXO 3
-- Create PopulationDepartement column in Departement 
-- It will be called by the user (main.py) 
 
CREATE OR REPLACE PROCEDURE CalculateDepartementPopulation(year integer)
AS $$
DECLARE
    dep RECORD; -- record to hold a row of the Departement table during iteration
BEGIN
    -- Create the necessary column in the table if they don't already exist
    BEGIN
        ALTER TABLE Departement ADD COLUMN PopulationDepartement FLOAT;
    EXCEPTION WHEN duplicate_column THEN
        -- Do nothing if the column already exists
        NULL;
    END;
    -- Calculate the population for each department
    FOR dep IN SELECT * FROM Departement LOOP
        UPDATE Departement
        SET PopulationDepartement = (
            SELECT SUM(Statistic.StatValue)
            FROM Commune
            INNER JOIN Statistic
                ON Commune.CodeCommune = Statistic.CodeCommune
            WHERE Commune.IdDepartement = dep.IdDepartement
            AND Indicator = 'Population'
            AND Category LIKE 'Population en %' 
            AND StartYear = year
            AND (EndYear IS NULL OR EndYear >= year)
        )
        WHERE IdDepartement = dep.IdDepartement;
    END LOOP;
    
END;
$$ LANGUAGE plpgsql;

-- Create PopulationRegion column in Region

CREATE OR REPLACE PROCEDURE CalculateRegionPopulation(year integer)
AS $$
DECLARE
    reg RECORD; -- record to hold a row of the Region table during iteration
BEGIN
    -- Create the necessary column in the table if they don't already exist
    BEGIN
        ALTER TABLE Region ADD COLUMN PopulationRegion FLOAT;
    EXCEPTION WHEN duplicate_column THEN
        -- Do nothing if the column already exists
        NULL;
    END;
    CALL CalculateDepartementPopulation(year); 
    -- Calculate the population for each region
    FOR reg IN SELECT * FROM Region LOOP
        UPDATE Region
        SET PopulationRegion = (
            SELECT SUM(PopulationDepartement)
            FROM Departement
            WHERE IdRegion = reg.IdRegion
        )
        WHERE IdRegion = reg.IdRegion;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CALL CalculateRegionPopulation(2019);

select * from Region;
SELECT * FROM Departement ;


ALTER TABLE Departement
DROP COLUMN PopulationDepartement;

ALTER TABLE region
DROP COLUMN PopulationRegion;