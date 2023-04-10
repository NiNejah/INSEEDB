drop table Region cascade ; 
drop table Departement cascade ; 
drop table Commune cascade ; 
drop table DeptChefLieu cascade ; 
drop table RegionChefLieu cascade ; 

create table Region (
    IdRegion INT PRIMARY KEY,
    NomRegion varchar(35) not null
);

create table Departement (
    IdDepartement INT PRIMARY KEY,
    NomDepartement varchar(35) not null,
    IdRegion INT references Region(IdRegion) not null
);

create table Commune (
    IdCommune varchar(5) PRIMARY KEY,
    NomCommune varchar(35) not null,
    IdDepartement INT references Departement(IdDepartement)
);

create table DeptChefLieu (
    IdCommune varchar(5) references Commune(IdCommune) ,
    IdDepartement INT references Departement(IdDepartement) ,
    PRIMARY KEY (IdCommune,IdDepartement)
);

create table RegionChefLieu (
    IdCommune varchar(5) references Commune(IdCommune) ,
    IdRegion INT references Region(IdRegion) ,
    PRIMARY KEY (IdCommune,IdRegion)
);

insert into Region( IdRegion , NomRegion ) values (1,'Guadeloupe');
insert into Departement (IdDepartement , NomDepartement , IdRegion ) values (1,'Ain',1);
insert into Commune (IdCommune, NomCommune, IdDepartement) values (01001,'L''Abergement-Clémenciat',1);
insert into DeptChefLieu (IdCommune,IdDepartement) values (01001,01);
insert into RegionChefLieu (IdCommune, IdRegion) values (01001,1);


-- select * from Region ;
-- select * from Departement ; 
-- select * from Commune ; 
-- select * from DeptChefLieu ; 
-- select * from RegionChefLieu ; 

