-- For Stored procedure EXO 3
-- Create PopulationDepartement column in Departement 
-- And PopulationRegion column in Region
-- It will be called by the user (main.py) 
 
CREATE OR REPLACE FUNCTION CalculatePopulation(years integer[])
RETURNS void AS $$
DECLARE
    dep RECORD; -- record to hold a row of the Departement table during iteration
    reg RECORD; -- record to hold a row of the Region table during iteration
BEGIN
    -- Create the necessary columns in the tables if they don't already exist
    BEGIN
        ALTER TABLE Departement ADD COLUMN IF NOT EXISTS PopulationDepartement FLOAT;
    END;
    
    BEGIN
        ALTER TABLE Region ADD COLUMN IF NOT EXISTS PopulationRegion FLOAT;
    END;

    FOREACH year IN ARRAY years LOOP
        -- Calculate the population for each department for the current year
        FOR dep IN SELECT * FROM Departement LOOP
            UPDATE Departement
            SET PopulationDepartement = (
                SELECT SUM(Statistic.StatValue)
                FROM Commune
                INNER JOIN Statistic
                    ON Commune.CodeCommune = Statistic.CodeCommune
                WHERE Commune.IdDepartement = dep.IdDepartement
                AND Indicator = 'Population'
                AND StartYear = year
                AND (EndYear IS NULL OR EndYear >= year)
            )
            WHERE IdDepartement = dep.IdDepartement;
        END LOOP;

        -- Calculate the population for each region for the current year
        FOR reg IN SELECT * FROM Region LOOP
            UPDATE Region
            SET PopulationRegion = (
                SELECT SUM(PopulationDepartement)
                FROM Departement
                WHERE CodeRegion = reg.CodeRegion
            )
            WHERE CodeRegion = reg.CodeRegion;
        END LOOP;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

CALL CalculatePopulation(array[2008, 2013, 2019]);
