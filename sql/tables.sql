-- DROP TABLE Region cascade ; 
-- DROP TABLE Departement cascade ; 
-- DROP TABLE Commune cascade ; 
-- DROP TABLE DeptChefLieu cascade ; 
-- DROP TABLE RegionChefLieu cascade ; 
-- DROP TABLE Statistic cascade ;

CREATE TABLE Region (
    IdRegion INT PRIMARY KEY,
    NameRegion VARCHAR(35) CONSTRAINT region_name_null NOT NULL
);

CREATE TABLE Departement (
    IdDepartement VARCHAR(3) PRIMARY KEY,
    NameDepartement VARCHAR(35) CONSTRAINT departement_name_null NOT NULL,
    IdRegion INT references Region(IdRegion) NOT NULL
);

CREATE TABLE Commune (
    -- IdCommune SERIAL PRIMARY KEY ,
    CodeCommune CHAR(5) UNIQUE,
    NameCommune VARCHAR(100) CONSTRAINT commune_name_null NOT NULL,
    IdDepartement VARCHAR(3) references Departement(IdDepartement)
);

CREATE TABLE DeptChefLieu (
    CodeCommune CHAR(5) references Commune(CodeCommune) ,
    IdDepartement VARCHAR(3) references Departement(IdDepartement) ,
    PRIMARY KEY (CodeCommune,IdDepartement)
);

CREATE TABLE RegionChefLieu (
    CodeCommune CHAR(5) references Commune(CodeCommune) ,
    IdRegion INT references Region(IdRegion) ,
    PRIMARY KEY (CodeCommune,IdRegion)
);


CREATE TABLE Statistic (
    IdStatistic SERIAL PRIMARY KEY,
    CodeCommune CHAR(5) REFERENCES Commune(CodeCommune),
    Indicator VARCHAR(50),
    Category VARCHAR(100),
    StartYear INT,
    EndYear INT NULL,
    StatValue FLOAT,
    -- Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (CodeCommune, Indicator, Category, StartYear, EndYear)
);