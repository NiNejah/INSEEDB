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


insert into Region( IdRegion , NameRegion ) values (1,'Region1');
insert into Region( IdRegion , NameRegion ) values (2,'Region2');
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values ('01','Departement1',1);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values ('02','Departement2',1);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values ('03','Departement3',2);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values ('04','Departement4',2);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values ('05','Departement5',1);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01001','Commune1','01');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01002','Commune2','01');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01003','Commune3','02');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01004','Commune4','02');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01005','Commune5','03');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01006','Commune6','04');
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01007','Commune8','05');
insert into DeptChefLieu (CodeCommune,IdDepartement) values ('01001', '01');
insert into DeptChefLieu (CodeCommune,IdDepartement) values ('01003','02');
insert into DeptChefLieu (CodeCommune,IdDepartement) values ('01005','03');
insert into DeptChefLieu (CodeCommune,IdDepartement) values ('01006','04');
insert into DeptChefLieu (CodeCommune,IdDepartement) values ('01007','05');
insert into RegionChefLieu (CodeCommune, IdRegion) values ('01003',1);
insert into RegionChefLieu (CodeCommune, IdRegion) values ('01005',2);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01001','Population','2019',2019,NULL,10000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01007','Population','2019',2019,NULL,5000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01007','Population','2019',2019,NULL,1000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01005','Population','2019',2019,NULL,5000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01002','Population','2019',2019,NULL,6000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01004','Population','2019',2019,NULL,8000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01003','Population','2019',2019,NULL,100);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01002','Population','Homme',2019,NULL,4000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01005','Population','2013',2013,NULL,20000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01006','Population',StatValue'2013',2013,NULL,1000);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01003','Population','0-14 ans',2013,NULL,2500);

insert into Statistic (CodeCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values ('01002','Naissances','entre 1975 et 1982',1975,1982,1250);

