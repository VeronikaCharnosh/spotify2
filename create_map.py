'''Map'''
import pycountry
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from main import for_return


def country(lst: list):
    '''
    >>> country(['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'])
    ['Andorra', 'United Arab Emirates', 'Antigua and Barbuda', 'Albania', 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan', 'Bosnia and Herzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia, Plurinational State of', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana', 'Belize', 'Canada', 'Congo, The Democratic Republic of the', 'Congo', 'Switzerland', "Côte d'Ivoire", 'Chile', 'Cameroon', 'Colombia', 'Costa Rica', 'Cabo Verde', 'Curaçao', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Spain', 'Ethiopia', 'Finland', 'Fiji', 'Micronesia, Federated States of', 'France', 'Gabon', 'United Kingdom', 'Grenada', 'Georgia', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea', 'Greece', 'Guatemala', 'Guinea-Bissau', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Comoros', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', 'Kazakhstan', "Lao People's Democratic Republic", 'Lebanon', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Montenegro', 'Madagascar', 'Marshall Islands', 'North Macedonia', 'Mali', 'Mongolia', 'Macao', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Palestine, State of', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Serbia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Suriname', 'Sao Tome and Principe', 'El Salvador', 'Eswatini', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Uzbekistan', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Vanuatu', 'Samoa', 'South Africa', 'Zambia', 'Zimbabwe']
    '''
    res = []
    for elem in lst:
        country = pycountry.countries.get(alpha_2=elem)
        if country is not None:
            res.append(country.name)
    return res[:75]

def get_coord(countries):
    '''
    >>> get_coord(['Andorra', 'United Arab Emirates', 'Antigua and Barbuda', 'Albania', 'Armenia', 'Angola', 'Argentina', 'Austria', 'Australia', 'Azerbaijan', 'Bosnia and Herzegovina', 'Barbados', 'Bangladesh', 'Belgium', 'Burkina Faso', 'Bulgaria', 'Bahrain', 'Burundi', 'Benin', 'Brunei Darussalam', 'Bolivia, Plurinational State of', 'Brazil', 'Bahamas', 'Bhutan', 'Botswana', 'Belize', 'Canada', 'Congo, The Democratic Republic of the', 'Congo', 'Switzerland', "Côte d'Ivoire", 'Chile', 'Cameroon', 'Colombia', 'Costa Rica', 'Cabo Verde', 'Curaçao', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Denmark', 'Dominica', 'Dominican Republic', 'Algeria', 'Ecuador', 'Estonia', 'Egypt', 'Spain', 'Ethiopia', 'Finland', 'Fiji', 'Micronesia, Federated States of', 'France', 'Gabon', 'United Kingdom', 'Grenada', 'Georgia', 'Ghana', 'Gambia', 'Guinea', 'Equatorial Guinea', 'Greece', 'Guatemala', 'Guinea-Bissau', 'Guyana', 'Hong Kong', 'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'Ireland', 'Israel', 'India', 'Iraq', 'Iceland', 'Italy', 'Jamaica', 'Jordan', 'Japan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Comoros', 'Saint Kitts and Nevis', 'Korea, Republic of', 'Kuwait', 'Kazakhstan', "Lao People's Democratic Republic", 'Lebanon', 'Saint Lucia', 'Liechtenstein', 'Sri Lanka', 'Liberia', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Libya', 'Morocco', 'Monaco', 'Moldova, Republic of', 'Montenegro', 'Madagascar', 'Marshall Islands', 'North Macedonia', 'Mali', 'Mongolia', 'Macao', 'Mauritania', 'Malta', 'Mauritius', 'Maldives', 'Malawi', 'Mexico', 'Malaysia', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand', 'Oman', 'Panama', 'Peru', 'Papua New Guinea', 'Philippines', 'Pakistan', 'Poland', 'Palestine, State of', 'Portugal', 'Palau', 'Paraguay', 'Qatar', 'Romania', 'Serbia', 'Rwanda', 'Saudi Arabia', 'Solomon Islands', 'Seychelles', 'Sweden', 'Singapore', 'Slovenia', 'Slovakia', 'Sierra Leone', 'San Marino', 'Senegal', 'Suriname', 'Sao Tome and Principe', 'El Salvador', 'Eswatini', 'Chad', 'Togo', 'Thailand', 'Tajikistan', 'Timor-Leste', 'Tunisia', 'Tonga', 'Turkey', 'Trinidad and Tobago', 'Tuvalu', 'Taiwan, Province of China', 'Tanzania, United Republic of', 'Ukraine', 'Uganda', 'United States', 'Uruguay', 'Uzbekistan', 'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Vanuatu', 'Samoa', 'South Africa', 'Zambia', 'Zimbabwe'])
    [['Andorra', (42.5407167, 1.5732033)]]
    '''
    print(len(countries))
    geolocator = Nominatim(user_agent="My_application")
    addresses = []
    for country in countries:
        location =  RateLimiter(geolocator.geocode, min_delay_seconds=1)(country)
        if location is not None:
            address = [location.address, (location.latitude, location.longitude)]
            addresses.append(address)
    return addresses

def create_map(coords, result_of_search):
    '''
    >>> create_map([['Andorra', (42.5407167, 1.5732033)], ['Antigua and Barbuda', (17.2234721, -61.9554608)], ['Shqipëria', (41.000028, 19.9999619)], ['Հայաստան', (40.7696272, 44.6736646)], ['Angola', (-11.8775768, 17.5691241)], ['Argentina', (-34.9964963, -64.9672817)], ['Österreich', (47.59397, 14.12456)], ['Australia', (-24.7761086, 134.755)], ['Azərbaycan', (40.3936294, 47.7872508)], ['Bosna i Hercegovina / Босна и Херцеговина', (44.3053476, 17.5961467)], ['Barbados', (13.1500331, -59.5250305)], ['বাংলাদেশ', (24.4769288, 90.2934413)], ['België / Belgique / Belgien', (50.6402809, 4.6667145)], ['Burkina Faso', (12.0753083, -1.6880314)], \
['България', (42.6073975, 25.4856617)], ['البحرين', (26.1551249, 50.5344606)], ['Burundi', (-3.426449, 29.9324519)], ['Bénin', (9.5293472, 2.2584408)], ['Brunei', (4.4137155, 114.5653908)], ['Bolivia', (-17.0568696, -64.9912286)], ['Brasil', (-10.3333333, -53.2)], ['The Bahamas', (24.7736546, -78.0000547)], ['འབྲུག\
ཡུལ་', (27.549511, 90.5119273)], ['Botswana', (-23.1681782, 24.5928742)], ['Belize', (16.8259793, -88.7600927)], ['Canada', (61.0666922, -107.991707)], ['Répu\
blique démocratique du Congo', (-2.9814344, 23.8222636)], ['République démocratique du Congo', (-2.9814344, 23.8222636)], ['Schweiz/Suisse/Svizzera/Svizra', (46.7985624, 8.2319736)], ['Côte d’Ivoire', (7.9897371, -5.5679458)], ['Chile', (-31.7613365, -71.3187697)], ['Cameroun', (4.6125522, 13.1535811)], ['Colombia', (4.099917, -72.9088133)], ['Costa Rica', (10.2735633, -84.0739102)], ['Cabo Verde', (16.0000552, -24.0083947)], ['Curaçao, Nederland', (12.21339425, -69.0408499890865)], ['Κύπρος - Kıbrıs', (34.9823018, 33.1451285)], ['Česko', (49.7439047, 15.3381061)], ['Deutschland', (51.1638175, 10.4478313)], ['Djibouti جيبوتي', (11.8145966, 42.8453061)], ['Danmark', (55.670249, 10.3333283)], ['República Dominicana', (19.0974031, -70.3028026)], ['República Dominicana', (19.0974031, -70.3028026)], ['Algérie / ⵍⵣⵣⴰⵢⴻⵔ / الجزائر', (28.0000272, 2.9999825)], ['Ecuador', (-1.3397668, -79.3666965)], ['Eesti', (58.7523778, 25.3319078)], ['مصر', (26.2540493, 29.2675469)], ['España', (39.3260685, -4.8379791)], ['ኢትዮጵያ', (10.2116702, 38.6521203)], ['Suomi / Finland', (63.2467777, 25.9209164)], ['Viti', (-18.1239696, 179.0122737)], ['Micronesia', (8.6062347, 151.832744331612)], ['France', (46.603354, 1.8883335)], ['Gabon', (-0.8999695, 11.6899699)], ['United Kingdom', (54.7023545, -3.2765753)], ['Grenada', (12.1360374, -61.6904045)], ['Georgia, United States', (32.3293809, -83.1137366)], ['Ghana', (8.0300284, -1.0800271)], ['Gambia', (13.470062, -15.4900464)], ['Guinée', (10.7226226, -10.7083587)], ['Guinea Ecuatorial', (1.613172, 10.5170357)], ['Ελλάς', (38.9953683, \
21.9877132)], ['Guatemala', (15.5855545, -90.345759)], ['Guiné-Bissau', (11.815215, -15.2351044)], ['Guyana', (4.8417097, -58.6416891)], ['香港島 Hong Kong Island, 香港 Hong Kong, 中国', (22.2793278, 114.1628131)], ['Honduras', (15.2572432, -86.0755145)], ['Hrvatska', (45.3658443, 15.6575209)], ['Ayiti', (19.1399952, -72.3570972)], ['Magyarország', (47.1817585, 19.5060937)], ['Indonesia', (-2.4833826, 117.8902853)], ['Éire / Ireland', (52.865196, -7.9794599)], ['ישראל', (30.8124247, 34.8594762)], ['India', (22.3511148, 78.6677428)], ['العراق', (33.0955793, 44.1749775)], ['Ísland', (64.9841821, -18.1059013)], ['Italia', (42.6384261, 12.674297)], ['Jamaica', (18.1850507, -77.3947693)], ['الأردن', (31.1667049, 36.941628)], ['日本', (36.5748441, 139.2394179)], ['Kenya', (1.4419683, 38.4313975)], ['Кыргызстан', (41.5089324, 74.724091)], ['ព្រះរាជាណាចក្រ\u200bកម្ពុជា', (12.5433216, 104.8144914)], ['Kiribati', (0.3448612, 173.6641773)], ['Co\
mores Komori جزر القمر', (-12.2045176, 44.2832964)], ['Saint Kitts and Nevis', (17.250512, -62.6725973)], ['Корея, проспект Фатыха Амирхана, Ново-Савиновский \
район, городской округ Казань, Татарстан, Приволжский федеральный округ, 420126, Россия', (55.8215537, 49.132971)], ['الكويت', (29.2733964, 47.4979476)], ['Қазақстан', (48.1012954, 66.7780818)], ['ປະເທດລາວ', (20.0171109, 103.378253)], ['لبنان', (33.8750629, 35.843409)]],['TVORCHI', 'Heart of Steel', '0jWniZlqlLCZY3xSPwPXz5', ['AD']])
    '''
    html = '''<h4>Song info:</h4>
    Name: {},<br>
    Artist: {},
    Country: {}
    '''
    map = folium.Map(tiles="Stamen Terrain", zoom_start = 5)
    fg = folium.FeatureGroup(name='countries')
    for elem in coords:
        lat = elem[1][0]
        lon = elem[1][1]
        iframe = folium.IFrame(html=html.format(result_of_search[1], result_of_search[0], elem[0]),
                          width=300,
                          height=100)
        fg.add_child(folium.Marker(location=[lat, lon],
                                    popup=folium.Popup(iframe),
                                    icon=folium.Icon(icon= 'check', color= 'red')))
    map.add_child(fg)
    map.add_child(folium.LayerControl())
    map.save("templates/Result_map.html")

def result(name):

    res_of_main = for_return(name)
    # print(res_of_main)
    # converted_countries = country(res_of_main[3])
    # print(converted_countries)
    coords = get_coord(res_of_main[3])
    create_map(coords, res_of_main)


# if __name__ == '__main__':
#     import doctest 
#     print(doctest.testmod())