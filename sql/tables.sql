drop table Region cascade ; 
drop table Departement cascade ; 
drop table Commune cascade ; 
drop table DeptChefLieu cascade ; 
drop table RegionChefLieu cascade ; 

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
    IdCommune CHAR(5) PRIMARY KEY,
    NameCommune VARCHAR(35) CONSTRAINT commune_name_null NOT NULL,
    IdDepartement INT references Departement(IdDepartement)
);

create table DeptChefLieu (
    IdCommune CHAR(5) references Commune(IdCommune) ,
    IdDepartement INT references Departement(IdDepartement) ,
    PRIMARY KEY (IdCommune,IdDepartement)
);

create table RegionChefLieu (
    IdCommune CHAR(5) references Commune(IdCommune) ,
    IdRegion INT references Region(IdRegion) ,
    PRIMARY KEY (IdCommune,IdRegion)
);


create table Statistic (
    IdStat INT PRIMARY KEY,
    IdCommune CHAR(5) references Commune(IdCommune),
    from DATE CONSTRAINT from_date_null NOT NULL ,
    To DATE ,
    lable VARCHAR(50) CONSTRAINT lable_null NOT NULL ,
    statNum FLOAT CONSTRAINT statNum_positives check (statNum >= 0)
);

insert into Region( IdRegion , NameRegion ) values (1,'Guadeloupe');
insert into Departement (IdDepartement , NameDepartement , IdRegion ) values (1,'Ain',1);
insert into Commune (IdCommune, NameCommune, IdDepartement) values (01001,'L''Abergement-Clémenciat',1);
insert into DeptChefLieu (IdCommune,IdDepartement) values (01001,01);
insert into RegionChefLieu (IdCommune, IdRegion) values (01001,1);


-- select * from Region ;
-- select * from Departement ; 
-- select * from Commune ; 
-- select * from DeptChefLieu ; 
-- select * from RegionChefLieu ; 

