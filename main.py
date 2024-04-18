import csv
import random
from datetime import datetime

from constants import FILE, AD_TYPE, FIELDNAMES, TARGET_AUDIENCE, SEASONS, ORGANIZATIONS, YEARS


def generate_ads():
    start_organisations = 16
    with open(FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
    for year in YEARS:
        for i in range(300):
            day = random.randint(1, 28)
            month = random.randint(1, 12)
            
            season = random.choice(SEASONS.get(random.choice(list(SEASONS.keys()))))
            organisation = random.choice(ORGANIZATIONS[:start_organisations])
            ad_type = random.choice(list(AD_TYPE.keys()))
            duration_in_seconds = random.randint(15, 120)
            
            if season == 'Christmas':
                day = 25
                month = 12
            
            if season == 'New Year':
                day = 1
                month = 1
            
            if season == 'Valentine\'s Day':
                day = 14
                month = 2

            if season == 'Easter':
                day = random.randint(25,31)
                month = 3

            date = datetime(year, month, day).date().strftime('%d %B, %Y')
        
            if duration_in_seconds < 70:
                cost = random.randint(AD_TYPE.get(ad_type).get('min'), AD_TYPE.get(ad_type).get('max')//2)
            else:
                cost = random.randint(AD_TYPE.get(ad_type).get('max')//2, AD_TYPE.get(ad_type).get('max'))

            times_run = random.randint(10, 100)
            
            target_audience = random.choice(TARGET_AUDIENCE)
            
            reach = random.randint(40000, 400000)
            
            response_rate = round(random.random(), 2)
            
            ad_to_lead_rate = round(random.randint(0, int(response_rate*100)) / 100, 2)
            
            sales_impact = random.randint(10000, 1000000)
            
            with open(FILE, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
                writer.writerow({
                    'date': date,
                    'season': season,
                    'organisation': organisation,
                    'ad_type': ad_type,
                    'duration_in_seconds': duration_in_seconds,
                    'cost': cost,
                    'times_run': times_run,
                    'target_audience': target_audience,
                    'reach': reach,
                    'response_rate': response_rate,
                    'ad_to_lead_rate': ad_to_lead_rate,
                    'sales_impact': sales_impact
                })
                
        start_organisations += 8


if __name__ == '__main__':
    generate_ads()
    print('Ads generated successfully!')
