CREATE TABLE Statistic (
    Id INT SERIAL PRIMARY KEY,
    IdCommune INT REFERENCES Commune(IdCommune), 
    Indicator VARCHAR(50) NOT NULL,
    Category VARCHAR(50) NOT NULL,
    StartYear INT NOT NULL,
    EndYear INT,
    StatValue INT NOT NULL,
    CONSTRAINT valid_indicator CHECK (Indicator IN ('Population', 'Births', 'Deaths', 'Migration')),
    CONSTRAINT valid_population_category CHECK (Indicator = 'Population' AND Category IN ('0-14 years', '15-29 years', '30-44 years', '45-59 years', '60-74 years', '75-89 years', '90+ years')),
    CONSTRAINT valid_births_category CHECK (Indicator = 'Births' AND Category IN ('0-1 years', '1-4 years', '5-9 years', '10-14 years', '15-19 years', '20-24 years', '25-29 years', '30-34 years', '35-39 years', '40-44 years', '45-49 years', '50-54 years', '55-59 years', '60-64 years', '65-69 years', '70-74 years', '75-79 years', '80-84 years', '85-89 years', '90+ years')),
    CONSTRAINT valid_deaths_category CHECK (Indicator = 'Deaths' AND Category IN ('0-1 years', '1-4 years', '5-9 years', '10-14 years', '15-19 years', '20-24 years', '25-29 years', '30-34 years', '35-39 years', '40-44 years', '45-49 years', '50-54 years', '55-59 years', '60-64 years', '65-69 years', '70-74 years', '75-79 years', '80-84 years', '85-89 years', '90+ years')),
    CONSTRAINT valid_migration_category CHECK (Indicator = 'Migration' AND Category IN ('In-migration', 'Out-migration')),
    CONSTRAINT valid_start_year CHECK (StartYear >= 1900),
    CONSTRAINT valid_end_year CHECK (EndYear IS NULL OR EndYear >= StartYear)
);
