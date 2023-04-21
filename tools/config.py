DBNAME = "insee"
USERNAME="postgres"
PASS="1111"

TABLE_COLUMNS = {
    'Region' : ['IdRegion' , 'NameRegion'],
    'Departement': ['IdDepartement','IdRegion','NameDepartement'],
    'Commune' : ['CodeCommune','IdDepartement','NameCommune'],
    'RegionChefLieu' :  ['CodeCommune' , 'IdRegion'],
    'DeptChefLieu' :  ['CodeCommune' , 'IdDepartement'],
    'Statistic' : ['CodeCommune','Indicator','Category','StartYear','EndYear','StatValue']
}