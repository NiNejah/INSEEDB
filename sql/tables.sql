drop table Region cascade ; 
drop table Departement cascade ; 
drop table Commune cascade ; 
drop table DeptChefLieu cascade ; 
drop table RegionChefLieu cascade ; 
drop table Statistic cascade ;

create table Region (
    IdRegion INT PRIMARY KEY,
    NameRegion VARCHAR(35) CONSTRAINT region_name_null NOT NULL
);

create table Departement (
    IdDepartement INT PRIMARY KEY,
    NameDepartement VARCHAR(35) CONSTRAINT departement_name_null NOT NULL,
    IdRegion INT references Region(IdRegion) NOT NULL
);

create table Commune (
    IdCommune SERIAL PRIMARY KEY ,
    CodeCommune CHAR(5),
    NameCommune VARCHAR(35) CONSTRAINT commune_name_null NOT NULL,
    IdDepartement INT references Departement(IdDepartement)
);

create table DeptChefLieu (
    IdCommune INT references Commune(IdCommune) ,
    IdDepartement INT references Departement(IdDepartement) ,
    PRIMARY KEY (IdCommune,IdDepartement)
);

create table RegionChefLieu (
    IdCommune INT references Commune(IdCommune) ,
    IdRegion INT references Region(IdRegion) ,
    PRIMARY KEY (IdCommune,IdRegion)
);


CREATE TABLE Statistic (
    IdStatistic SERIAL PRIMARY KEY,
    IdCommune INT REFERENCES Commune(IdCommune),
    Indicator VARCHAR(50),
    Category VARCHAR(50),
    StartYear INT,
    EndYear INT,
    StatValue INT,
    -- Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (IdCommune, Indicator, Category, StartYear, EndYear)
);

insert into Region( IdRegion , NameRegion ) values (1,'Region1');
insert into Region( IdRegion , NameRegion ) values (2,'Region2');
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (1,'Departement1',1);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (2,'Departement2',1);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (3,'Departement3',2);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (4,'Departement4',2);
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (5,'Departement5',1);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01001','Commune1',1);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01002','Commune2',1);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01003','Commune3',2);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01004','Commune4',2);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01005','Commune5',3);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01006','Commune6',4);
insert into Commune (CodeCommune, NameCommune, IdDepartement) values ('01007','Commune8',5);
insert into DeptChefLieu (IdCommune,IdDepartement) values (8,1);
insert into DeptChefLieu (IdCommune,IdDepartement) values (11,2);
insert into DeptChefLieu (IdCommune,IdDepartement) values (12,3);
insert into DeptChefLieu (IdCommune,IdDepartement) values (12,4);
insert into DeptChefLieu (IdCommune,IdDepartement) values (14,5);
insert into RegionChefLieu (IdCommune, IdRegion) values (8,1);
insert into RegionChefLieu (IdCommune, IdRegion) values (13,2);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (8,'Population','2019',2019,NULL,10000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (9,'Population','2019',2019,NULL,5000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (10,'Population','2019',2019,NULL,1000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (11,'Population','2019',2019,NULL,5000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (12,'Population','2019',2019,NULL,6000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (13,'Population','2019',2019,NULL,8000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (14,'Population','2019',2019,NULL,100);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (8,'Population','Homme',2019,NULL,4000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (9,'Population','2013',2013,NULL,20000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (11,'Population','2013',2013,NULL,1000);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (11,'Population','0-14 ans',2013,NULL,2500);

insert into Statistic (IdCommune,Indicator,Category,StartYear,EndYear,StatValue) 
values (12,'Naissances','entre 1975 et 1982',1975,1982,1250);

select * from Region ;
select * from Departement ; 
select * from Commune ; 
select * from DeptChefLieu ; 
select * from RegionChefLieu ; 
select * from Statistic ; 