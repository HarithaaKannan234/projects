select*from PortfolioProj1..covidDeaths
where continent is not null
order by 3,4
select*from PortfolioProj1..covidVaccinations
order by 3,4

Select location,date,total_cases,new_cases,total_deaths,population
from PortfolioProj1..covidDeaths
where continent is not null
order by 1,2

-- total cases vs total deaths
Select location,date,total_cases,total_deaths,(cast(total_deaths as float))/cast(total_cases as float) *100 as deathPercentage 
from PortfolioProj1..covidDeaths
where location='India' and continent is not null
order by 1,2
--total cases vs population 
Select location,date,total_cases,population, (cast(total_cases as float))/cast(population as float) *100 as infectedPercentage 
from PortfolioProj1..covidDeaths
where location='India' and total_cases is not null and continent is not null
order by 1,2

--countries with highest infection rate compared to population
Select location, MAX(total_cases) as highestInfectionRate,population,MAX(cast(total_cases as float)/cast(population as float)) *100 as percentOfPopulationInfected
from PortfolioProj1..covidDeaths
where  total_cases is not null and continent is not null
GROUP BY
    location, population
order by percentOfPopulationInfected desc
--showing countries with highest death count per population
Select location, Max(cast(total_deaths as int)) as totalDeathCount
from PortfolioProj1..covidDeaths
where  total_cases is not null and continent is not null 
GROUP BY
    location
order by totalDeathCount desc

--breaking things down by continent

--showing continents with highest death count
Select continent, Max(cast(total_deaths as int)) as totalDeathCount
from PortfolioProj1..covidDeaths
where  total_cases is not null and continent is not null 
GROUP BY
   continent
order by totalDeathCount desc

--global numbers 

Select date,sum (new_cases) as casesPerDay, sum (new_deaths) as deathsPerDay,
case when 
sum(new_cases)= 0 then null
else sum(new_deaths)/sum(new_cases)*100
end as deathPercPerDay
from PortfolioProj1..covidDeaths
where  continent is not null
group by 
date
order by 1,2

--joining
--total population vs vaccinations
Select dea.continent, dea.location , dea. date , dea.population, vac.new_vaccinations
, sum (cast(new_vaccinations as float))over (partition by dea.location order by dea.location , dea.date) as rollingVaccinationCounts
from PortfolioProj1..covidDeaths dea
join PortfolioProj1..covidVaccinations vac
on dea.location = vac.location
and dea.date = vac.date
where dea.continent is not null
order by  2, 3


--use cte
with popVSvac(continent, location , date, population, new_vaccinations, RollingPeopleVaccinated)
as(
Select dea.continent, dea.location , dea. date , dea.population, vac.new_vaccinations
, sum (convert(bigint,new_vaccinations ))over (partition by dea.location order by dea.location , dea.date) as RollingPeopleVaccinated
from PortfolioProj1..covidDeaths dea
join PortfolioProj1..covidVaccinations vac
on dea.location = vac.location
and dea.date = vac.date

where dea.continent is not null)
SELECT
   *,(RollingPeopleVaccinated/population)*100
	from popVSvac

	--view
create view  percentPopulationVacinated as 
Select dea.continent, dea.location , dea. date , dea.population, vac.new_vaccinations
, sum (cast(new_vaccinations as float))over (partition by dea.location order by dea.location , dea.date) as rollingVaccinationCounts
from PortfolioProj1..covidDeaths dea
join PortfolioProj1..covidVaccinations vac
on dea.location = vac.location
and dea.date = vac.date
where dea.continent is not null
select * from percentPopulationVacinated


CREATE VIEW tcVStd AS
SELECT
    location,
    date,
    total_cases,
    total_deaths,
    (CAST(total_deaths AS FLOAT) / CAST(total_cases AS FLOAT)) * 100 AS deathPercentage 
FROM
    PortfolioProj1..covidDeaths
WHERE
    location = 'India' AND continent IS NOT NULL;