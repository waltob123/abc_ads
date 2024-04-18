FILE = 'ads.csv'

FIELDNAMES = ['date', 'season', 'organisation', 'ad_type', 'duration_in_seconds', 'cost',
              'times_run', 'target_audience', 'reach', 'response_rate', 'ad_to_lead_rate', 'sales_impact']

AD_TYPE = {
    'TV Commercial': {'min': 50000, 'max': 100000}, 
    'Radio': {'min': 25000, 'max': 50000}, 
    'Social Media': {'min': 5000, 'max': 10000}, 
    'Youtube': {'min': 10000, 'max': 25000}
    }

YEARS = [2020, 2021, 2022]

TARGET_AUDIENCE = [
    'Children', 'Teenagers', 'Youth', 'Adults', 'Workers',
    'Civil Servants', 'University Students'
]

SEASONS = {
    'Holiday Seasons': [
        'Christmas', 'New Year', 'Valentine\'s Day', 'Easter'
    ],
    'Major Events': [
        'Election', 'AFCON', 'African Games', 'World Cup'
    ],
    'Minor Events': [
        'Anniversary', 'Product Lunch', 'Promotions'
    ],
    'No Season': [
        'No Season'
    ]
}

ORGANIZATIONS = [
    'MTN', 'Vodafone', 'AirtelTigo', 'Glo', 'Huawei', 'Samsung', 'Apple', 'Infinix', 'Tecno', 'Itel',
    'Ecobank', 'Access Bank', 'Franco Trading', 'Kinapharma', 'Melcom', 'Ernest Chemist', 'Kantanka',
    'Media General', 'EIB Network', 'Tobinco', 'FBN', 'Loyalty Insurance', 'Star Assurance', 'Glico',
    'Kasapreko', 'Papaye', 'Pizzaman', 'Lancaster Hotel', 'Acacia Health Insurance',
    'Ghana Rubber Estates Limited', 'Hisense', 'Fiesta Condoms'
    ]
