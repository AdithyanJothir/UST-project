# UST project

A brief description on how to run this project

## Deployment

Run these commands

```bash
pip install -r requirements.txt

cd Tasks

gunicorn -b localhost:<portnumber> serve:application --reload
```




## TASK1
#### Step 1 :
Go to Tasks/data.py and run it 
#### Step 2 :
Make sure that the data has been entered in the db
by running
```bash
use countries
country.find().pretty()
```

## TASK2

#### Step1:
```bash
cd Tasks
gunicorn -b localhost:<portnumber> serve:application --reload
````

#### Step2: (Question 2.1 countriesQuery)

```bash
query{
	countriesQuery(first:4,skip:3){
		name,
		countryId,
		capital,
		area,
		timezone,
		independance,
		continents,
		unMember,
        latlong{
			coordinates
		},
		languages,
		region,
		population
	}
}
````

#### Step3: (Question 2.2 countryQuery by id)

```bash
query{
	countryQuery(id:10){
		name,
		countryId,
		capital,
		area,
		timezone,
		independance,
		continents,
		unMember,
        latlong{
			coordinates
		},
		languages,
		region,
		population
	}
}
````

#### Step4: (Question 2.3 countriesNearbyQuery latlong)
 You are free to use any lat long value.
```bash
query{
	countriesNearby(loc: [-40,20]){
		name,
		countryId,
		capital,
		area,
		timezone,
		independance,
		continents,
		unMember,
		languages,
		latlong{
			coordinates
		},
		region,
		population
	}
}
````

#### Step5: (Question 2.4 countriesByLanguageQuery)
 You are free to use any language value.
```bash
query{
	countriesByLanguage(lang:"eng"){
		name,
		countryId,
		capital,
		area,
		timezone,
		independance,
		continents,
		unMember,
		languages,
		latlong{
			coordinates
		},
		region,
		population
	}
}
````

#### Step6: (Question 2.5 countryEditMutation)
```bash
mutation{
	countryEditMutation(countryId:10,area:5000,
	region:"Africa",population:10000)
	{
		country{
			area,
			region,
			population
		}
	}
}
````





