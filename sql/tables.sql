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
    IdDepartement VARCHAR(3) PRIMARY KEY,
    NameDepartement VARCHAR(35) CONSTRAINT departement_name_null NOT NULL,
    IdRegion INT references Region(IdRegion) NOT NULL
);

create table Commune (
    -- IdCommune SERIAL PRIMARY KEY ,
    CodeCommune CHAR(5) UNIQUE,
    NameCommune VARCHAR(100) CONSTRAINT commune_name_null NOT NULL,
    IdDepartement VARCHAR(3) references Departement(IdDepartement)
);

create table DeptChefLieu (
    CodeCommune CHAR(5) references Commune(CodeCommune) ,
    IdDepartement VARCHAR(3) references Departement(IdDepartement) ,
    PRIMARY KEY (CodeCommune,IdDepartement)
);

create table RegionChefLieu (
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

select * from Region ;
select * from Departement ; 
select * from Commune ; 
select * from DeptChefLieu ; 
select * from RegionChefLieu ; 
select * from Statistic ; 