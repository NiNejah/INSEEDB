-- Revoke modification permissions on tables
REVOKE INSERT, UPDATE, DELETE ON TABLE Region FROM public;
REVOKE INSERT, UPDATE, DELETE ON TABLE Departement FROM public;

-- Grant only SELECT permission to users
GRANT SELECT ON TABLE Region TO public;
GRANT SELECT ON TABLE Departement TO public;

-- Create a trigger function that calls the CalculatePopulation procedure
CREATE OR REPLACE FUNCTION update_population() RETURNS trigger AS $$
BEGIN
    IF (TG_OP = 'INSERT' OR TG_OP = 'UPDATE') THEN
        CALL CalculatePopulation(NEW.StartYear);
    ELSEIF (TG_OP = 'DELETE') THEN
        CALL CalculatePopulation(OLD.StartYear);
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger on the Statistic table
CREATE TRIGGER update_population_trigger
AFTER INSERT OR UPDATE OR DELETE ON Statistic
FOR EACH ROW
EXECUTE PROCEDURE update_population();
